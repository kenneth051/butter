from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import jwt
from datetime import datetime, timedelta
from butter.constants import agreement
from butter_uk import settings

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """Create and return a `User` with an email, username and password."""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, username, password, **extra_fields)
        return user
    
    
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, blank=False)
    username = models.EmailField(max_length=255, unique=False, blank=True)
    street = models.CharField(max_length=255, unique=True, blank=False)
    post_code = models.CharField(max_length=255, unique=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.email

    def token(self):
        credentials = {
            "id": self.id,
            "username": self.username,
            "is_staff": self.is_staff,
            "is_active": self.is_active,
            "is_superuser": self.is_superuser,
            "email": self.email,
            "exp": datetime.now() + timedelta(days=1)
        }
        return jwt.encode(credentials, settings.SECRET_KEY).decode("utf-8")

    
class UserTermsAgreement(models.Model):
    signed_user=models.ForeignKey(User, on_delete=models.CASCADE)
    signed_on = models.DateTimeField(auto_now=True)
    signed_agreement=models.TextField()
