from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    
    email = models.EmailField(unique=True)

    follows = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="UserFollows",
        related_name="followed_user",
        verbose_name="Abonnements"
    )


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    
    description = models.TextField(max_length=2048, blank=True)
    
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    
    image = models.ImageField(null=True, blank=True)
    
    time_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    ticket = models.ForeignKey(
        to=Ticket,
        on_delete=models.CASCADE)
    
    rating = models.PositiveSmallIntegerField( 
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    
    headline = models.CharField(max_length=128)
    
    body = models.TextField(max_length=8192, blank=True)
    
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following")
    
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by")
    
    def __repr__(self) -> str:
        return f"{self.user} s'est abonné à {self.followed_user}"

    class Meta:
        unique_together = ("user", "followed_user",)

    
        