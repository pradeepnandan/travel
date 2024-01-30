from django.db import models

# Create your models here.
class Places(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    des=models.TextField()

    def __str__(self): # to display the names in admin panel
        return self.name
class Team(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    desgn=models.CharField(max_length=250)
    def __str__(self):
        return self.desgn