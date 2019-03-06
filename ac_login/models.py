from django.db import models

# ac_login

class Login(models.Model):
    username =models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)
