from django.db import models

# Create your models here
class pt(models.Model):
    category=models.CharField(max_length=40,default="")
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    imag=models.ImageField(upload_to="ForHome",default="")
    description=models.CharField(max_length=100,default="this is the detail information about the product you choosed")
    
    def __str__(self):
        return self.name

class signop(models.Model):
    signid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40,default="")
    email=models.EmailField(max_length=80)
    pwOne=models.CharField(max_length=100)
    pwTwo=models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class contt(models.Model):
    contid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=80)
    phone_no=models.IntegerField()
    doubts=models.CharField(max_length=500)

    def __str__(self):
        return self.name
        