from django.db import models
from ac_admin.models import Department
from ac_login.models import Login
# ac_citizen



class CitizenRegister(models.Model):
    idno =models.IntegerField(primary_key=True)
    name =models.CharField(max_length=20)
    contact_number =models.IntegerField()
    address =models.TextField()
    city =models.CharField(max_length=20)
    Image =models.ImageField(upload_to='citizen/')
    username=models.ForeignKey(Login,on_delete=models.CASCADE)
#------------------------------------------------------------------------

class Compliants(models.Model):
    cid =models.IntegerField(primary_key=True)
    ctid =models.ForeignKey(CitizenRegister,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    message=models.TextField()
    image=models.ImageField(upload_to='compliants/')
    register_date=models.DateField()
    status=models.CharField(max_length=20)
    closing_date=models.DateField()
#--------------------------------------------------------------------------

class Feedback(models.Model):
    fid =models.IntegerField(primary_key=True)
    cid =models.ForeignKey(Compliants,on_delete=models.CASCADE)
    ctid =models.ForeignKey(CitizenRegister,on_delete=models.CASCADE)
    message=models.TextField()
    image=models.ImageField(upload_to='feedback/')