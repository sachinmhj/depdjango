from datetime import date
from django.db import models

# Create your models here.
class blug(models.Model):
    bgid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80,default="title here")
    dt = models.DateField(default=date.today)
    name = models.CharField(max_length=80,default="name here")
    desc = models.CharField(max_length=3000,default="")
    head = models.CharField(max_length=80,default="")
    chead = models.CharField(max_length=3000,default="")
    head2 = models.CharField(max_length=80,default="")
    chead2 = models.CharField(max_length=3000,default="")
    imaz1 = models.ImageField(upload_to="ForBlog",default="")
    imaz2 = models.ImageField(upload_to="ForBlog",default="")

    def __str__(self):
        return self.name

