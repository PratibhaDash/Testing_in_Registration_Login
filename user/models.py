from django.db import models

# Create your models here.
class RegistrationPage(models.Model):
    name= models.CharField(max_length=50,null=True)
    email= models.EmailField(max_length=100,null=True)
    mobile_no= models.CharField(max_length=100)
    address= models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=10,null=True)
    
    
    def __str__(self):
        return self.name