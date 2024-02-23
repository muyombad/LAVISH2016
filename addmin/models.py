from django.db import models


# Create your models here.


class otp_code(models.Model):
    code_otp = models.IntegerField()


class MTN(models.Model):
    campany = models.CharField(max_length=30, null=True)
    Credit = models.CharField(max_length=200)
    Debit = models.CharField(max_length=200)
    Name = models.CharField(max_length=100)
    R_Number = models.CharField(max_length=50)
    Phone_N = models.CharField(max_length=15)
    Available_Balance = models.CharField(max_length=5000)
    Time = models.DateTimeField()
    Maker = models.CharField(max_length=100, default='')


class AIRTELL(models.Model):
    campany = models.CharField(max_length=30, null=True)
    Credit = models.CharField(max_length=200)
    Debit = models.CharField(max_length=200)
    Name = models.CharField(max_length=100)
    R_Number = models.CharField(max_length=50)
    Phone_N = models.CharField(max_length=15)
    Available_Balance = models.CharField(max_length=5000)
    Time = models.DateTimeField()
    Maker = models.CharField(max_length=100)


class Had_cash(models.Model):
    stationary = models.IntegerField()
    agent = models.IntegerField()    


class Admin_state(models.Model):
    campany = models.CharField(max_length=200)   
    Credit = models.CharField(max_length=200)
    Debit = models.CharField(max_length=200) 
    Time = models.DateTimeField()
    balance = models.IntegerField()