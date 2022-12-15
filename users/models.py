from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, fullname, email, phone, password, **extra_fields):
        if not fullname:
            raise ValueError("Users must have a Firstname and Lastname")

        if not email:
            raise ValueError("Users must have an email address")

        if not phone:
            raise ValueError("Users must have a phone number")
        
        email = self.normalize_email(email)

        user = self.model(
            fullname=fullname,
            email=email,
            phone=phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, fullname, email, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser should have is_staff set to True")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser should have is_superuser set to True")

        return self.create_user(fullname=fullname, email=email, phone=phone, password=password, **extra_fields)
    

    # def _create_user(
    #     self, fullname, email, phone, password,  **extra_fields
    # ):
    #     if not fullname:
    #         raise ValueError("Users must have a Firstname and Lastname")

    #     if not email:
    #         raise ValueError("Users must have an email address")

    #     if not phone:
    #         raise ValueError("Users must have a phone number")

    #     now = timezone.now()
    #     email = self.normalize_email(email)

    #     user = self.model(
    #         fullname=fullname,
    #         email=email,
    #         phone=phone,
    #         is_staff=is_staff,
    #         is_active=True,
    #         is_superuser=is_superuser,
    #         last_login=now,
    #         date_joined=now,
    #         **extra_fields
    #     )

    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    # def create_user(self, fullname, email, phone, password, **extra_fields):
    #     return self._create_user(fullname, email, phone, password, False, False, **extra_fields)

    # def create_superuser(self, fullname, email, phone, password, **extra_fields):
    #     user = self._create_user(fullname, email, phone, password, True, True, **extra_fields)
    #     return user
    # pass


class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=100, verbose_name="Firstname Lastname", null=False, blank=False)
    
    email = models.EmailField(max_length=60, verbose_name="Email Address", unique=True)
    
    phone = models.CharField(max_length=11, verbose_name="11-digit Phone Number", null=True, blank=True, unique=False)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['fullname', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.fullname