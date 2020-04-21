from django.db import models

class Userregistrationmodel(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=40)
    email=models.EmailField()
    contactno=models.IntegerField(unique=True)
    companyname=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    status=models.CharField(max_length=20,default=False)

class Thoughtsmodel(models.Model):
    t_usernmae=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    t_contno=models.IntegerField(unique=True)

class Addeventmodel(models.Model):
    e_username=models.CharField(max_length=20)
    startdate=models.DateField()
    enddate=models.DateField()
    descr=models.CharField(max_length=100)
    contactno=models.IntegerField(unique=True)


