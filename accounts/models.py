from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from quiz import models as quiz

from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):
    """ User manager """

    def _create_user(self, username, password=None, department=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        if not username:  # check for an empty email
            raise AttributeError("User must set an Username")
        # else:  # normalizes the provided email
        #     email = self.normalize_email(email)
        
        # create user
        user = self.model(username=username, **extra_fields)

        if department:
            user.department = department
        else:
            # set default department here
            user.department = quiz.department.objects.get(pk=1)

        user.set_password(password)  # hashes/encrypts password
        user.save(using=self._db)  # safe for multiple databases
        return user

    def create_user(self, username, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_staffuser(self, username, password=None, **extra_fields):
        """Creates and returns a new staffuser using an email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        """Creates and returns a new superuser using an email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model """

    username = models.CharField(
        _("Roll NO"),
        max_length=10,
        unique=True
    )
    email = models.EmailField(
        _("Email Address"),
        max_length=255,
        unique=True,
        help_text="Ex: example@example.com",
        error_messages ={
            "unique":"A User with this email address already exists."
        }
    )
    department = models.ForeignKey(quiz.department, verbose_name=_("Department"), on_delete=models.SET_NULL,null=True)
    is_staff = models.BooleanField(_("Staff status"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    created_at = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Last Updated"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }