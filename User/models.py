from django.db import models
from datetime import timedelta
from django.utils import timezone
from User.managers import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import jwt
from ecom.settings import JWT_SECRET
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(db_index=True, max_length=255, unique=True)

    email = models.EmailField(db_index=True, unique=True)
   
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(default=timezone.now())

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    
    objects = UserManager()

    def __str__(self):     
        return self.email

    def get_name(self):
        return self.username


    @property
    def token(self):
        # expiration time 
        expiration_time = timezone.now() + timedelta(hours=10)
        
        payload = {
            'user_id': self.pk,
            'email': self.email,
            'exp': expiration_time,
            
        }

        # using the RS256 algorithm
        token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')

        return token