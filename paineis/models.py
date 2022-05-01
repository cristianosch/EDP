from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Quantities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        

class Counter(models.Model):     
    quantity = models.IntegerField(default='0', blank=True)
    quantities = models.IntegerField(default='0', blank=True,)
    date = models.DateField(auto_now_add=False, auto_now=True) 
    values_to_receive = models.FloatField(default='0', blank=True, null=True) 
    total = models.IntegerField(default='0', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    export_to_CSV = models.BooleanField(default=False)   
    total_to_receive = models.FloatField(default='0', blank=True, null=True) 

    def __str__(self):
        return str(self.quantities) + ' ' + str(self.date) + ' ' + str(self.total) + ' ' + str(self.total_to_receive)

        

 





