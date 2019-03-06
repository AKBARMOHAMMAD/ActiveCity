from django.db import models

# ac_admin.
class Department(models.Model):
    name=models.CharField(max_length=20,primary_key=True)