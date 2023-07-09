from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)    

class Device(models.Model):
    model = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    sn = models.IntegerField()
    condition = models.CharField(max_length=50)
class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)    
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)  
    check_out = models.DateTimeField(auto_now=False, auto_now_add=False)
    check_in = models.DateTimeField(auto_now=False, auto_now_add=False)
    out_condition = models.CharField(max_length=50)
    in_condition = models.CharField(max_length=50)   