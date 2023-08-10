from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image


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
    title = models.CharField(max_length=128, verbose_name="Titre")
    
    description = models.TextField(max_length=2048, blank=True)
    
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    
    image = models.ImageField(null=True, blank=True)
    
    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (200, 400)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Review(models.Model):
    ticket = models.ForeignKey(
        to=Ticket,
        on_delete=models.CASCADE)
    
    rating = models.PositiveSmallIntegerField( 
        validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="Note")
    
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    
    headline = models.CharField(max_length=128, verbose_name="Titre")
    
    body = models.TextField(max_length=8192, blank=True, verbose_name="Commentaire")
    
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

    
        