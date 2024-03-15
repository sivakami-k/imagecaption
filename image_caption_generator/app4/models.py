from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    status_choice=(('accepted','accepted'),('rejected','rejected'),('pending','pending'))
    Status=models.CharField(choices=status_choice,default='pending',max_length=200)


class Parent(models.Model):
    login=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    dob=models.CharField(max_length=200)
    gender=models.CharField(max_length=10)
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pin=models.IntegerField()
    phone=models.CharField(max_length=100)
  

class Child(models.Model):
    login=models.ForeignKey(Login,on_delete=models.CASCADE)
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    disability_type = models.CharField(max_length=20)
    disability_percentage = models.IntegerField()
    

class Awareness(models.Model):
    instructions=models.CharField(max_length=300,null=True,blank=True)
    awareness_videos=models.FileField(null=True,blank=True)

class Review(models.Model):
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    review=models.CharField(max_length=500)


