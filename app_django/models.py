from django.db import models
from passlib.hash import pbkdf2_sha256 as pbkdf
from datetime import timedelta
from django.utils import timezone
import os

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length = 32)
    password_hash = models.CharField(max_length = 128)
    token = models.CharField(max_length = 128)
    token_expiry = models.DateTimeField(null=True)

    def set_password(self, password):
        self.password_hash = pbkdf.hash(password)
        return

    def check_password(self, password):
        return pbkdf.verify(password, self.password_hash)

    def get_token(self):
        self.token = os.urandom(3).hex()
        self.token_expiry = timezone.now() + timedelta(seconds = 360)
        return self.token

    def validate_token(self):
        return (timezone.now() + timedelta(seconds = 60)) < self.token_expiry

class Employee(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    ed=models.CharField(max_length=32)
    role=models.CharField(max_length=32)
