from django.db import models
from ac_admin.models import department
from ac_login.models import login


# ac_officer

class officer(models.Model):
    idno =models.IntegerField(primary_key=True)
    name =models.CharField(max_length=20)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    contact_number =models.IntegerField()
    image=models.ImageField(upload_to='officer/')
    username=models.ForeignKey(login,on_delete=models.CASCADE)
