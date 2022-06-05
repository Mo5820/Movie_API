from django.db import models

# Create your models here.
class Moive(models.Model):
    hall=models.IntegerField()
    moive=models.CharField(max_length=15)
    data=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.moive

class Geust(models.Model):
    name=models.CharField(max_length=15)
    mobile=models.CharField(max_length=10)
    

    def __str__(self):
        return self.name

class Reserivation(models.Model):
    geust=models.ForeignKey(Geust ,related_name="reservation",on_delete=models.CASCADE)
    moive=models.ForeignKey(Moive ,related_name="reservation",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.moive