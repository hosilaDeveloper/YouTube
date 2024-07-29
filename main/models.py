from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Tag(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(null=True, blank=True)
    manage = models.TextField()

    def __str__(self):
        return self.name


class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=212)
    video = models.URLField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='video/')
    description = models.TextField()

    def __str__(self):
        return self.title
