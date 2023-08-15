from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image


class User(AbstractUser):
    """Registered website user."""
    username = models.CharField(max_length=15, unique=True)

    email = models.EmailField(unique=True)

    follows = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="UserFollows",
        related_name="followed_user",
        verbose_name="Abonnements",
    )


class Ticket(models.Model):
    """Request for one article / book review."""
    title = models.CharField(max_length=128, verbose_name="Titre")

    description = models.TextField(max_length=2048, blank=True)

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    image = models.ImageField(null=True, blank=True)

    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (200, 400)

    def resize_image(self):
        """Resizes then saves images uploaded by the users.
        The dimensions are set in the IMAGE_MAX_SIZE constant.
        """
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        """Extends the save method to systematically resize uploaded images
        whenever a Ticket is created.
        """
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()


class Review(models.Model):
    """Feedback about a given book or article.
    Systematically linked to a Ticket object.
    """
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)

    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Note")

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    headline = models.CharField(max_length=128, verbose_name="Titre")

    body = models.TextField(max_length=8192,
                            blank=True,
                            verbose_name="Commentaire")

    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    """Self-created object whenever an user follows another one."""
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following")

    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by")

    class Meta:
        unique_together = (
            "user",
            "followed_user",
        )
