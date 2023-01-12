from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField(max_length=300)
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class testmonials(models.Model):
    name=models.CharField(max_length=100,blank=True)
    desc=models.TextField()
    img=models.ImageField(upload_to='picture')
    number=models.IntegerField()
    def __str__(self) :
        return self.name  

