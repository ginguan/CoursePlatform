from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ("male", "men"),
    ("female", "women")
)


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="nickname", default="")
    birthday = models.DateField(verbose_name="birthday", null=True, blank=True)
    gender = models.CharField(verbose_name="gender", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="address", default="")
    mobile = models.CharField(max_length=10, unique=True, verbose_name="phone")
    image = models.ImageField(upload_to="head_image/%Y/%m", default="default.jpg")

    class Meta:
        verbose_name = "user_info"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
