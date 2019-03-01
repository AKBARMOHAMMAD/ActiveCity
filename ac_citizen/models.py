from django.db import models
from ac_admin.models import department
from ac_login.models import login
# ac_citizen



class citizenRegister(models.Model):
    idno =models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    contact_number=models.IntegerField()
    address=models.TextField()
    city=models.CharField(max_length=20)
    image=models.ImageField(upload_to='citizen/')
    username=models.ForeignKey(login,on_delete=models.CASCADE)

class complaints(models.Model):
    cid =models.IntegerField(primary_key=True)
    ctid=models.ForeignKey(citizenRegister,on_delete=models.CASCADE)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    message=models.TextField()
    image=models.ImageField(upload_to='complaints/')
    registration_date=models.DateField()
    status=models.CharField(max_length=15)
    closing_date=models.DateField()

class feedback(models.Model):
    fid=models.IntegerField(primary_key=True)
    cid=models.ForeignKey(complaints,on_delete=True)
    ctid=models.ForeignKey(citizenRegister,on_delete=True)
    message=models.TextField()
    image=models.ImageField(upload_to='feedback/')
