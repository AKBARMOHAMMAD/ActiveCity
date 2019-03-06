from django.db import models
from ac_admin.models import Department
from ac_login.models import Login
#ac_officers



class Officers(models.Model):
    idno =models.IntegerField(primary_key=True)
    name =models.CharField(max_length=20)
    department =models.ForeignKey(Department,on_delete=models.CASCADE)
    contact_number =models.IntegerField()
    image =models.ImageField(upload_to='officers/')
    username=models.ForeignKey(Login,on_delete=models.CASCADE)