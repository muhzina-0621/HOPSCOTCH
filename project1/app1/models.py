from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.CharField(max_length=100 , primary_key=True)
    password=models.CharField(max_length=100 , null=True)
    status=models.CharField(max_length=100 , null=True,default="pending")
    usertype=models.CharField(max_length=100,null=True)

class Reg(models.Model):    
    name=models.CharField(max_length=100,null=True)
    email=models.ForeignKey(Login,on_delete=models.CASCADE,max_length=100,null=True)
    age=models.CharField(max_length=100,null=True)
    grade=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)

# class Marks(models.Model):
#     emailid=models.EmailField(max_length=100,null=True)
#     reading=models.CharField(max_length=100, default="0")
#     dictation=models.CharField(max_length=100,default="0")
#     match=models.CharField(max_length=100, default="0")
#     comprehension=models.CharField(max_length=100,default="0")
#     fill=models.CharField(max_length=100, default="0")
#     count=models.CharField(max_length=100,default="0")
#     currency=models.CharField(max_length=100, default="0")
#     order=models.CharField(max_length=100,default="0")
#     arithmetic=models.CharField(max_length=100, default="0")
#     compare=models.CharField(max_length=100,default="0")
#     questionnaire=models.CharField(max_length=100, default="0")
#     result=models.CharField(max_length=100,default="0")

class Mark(models.Model):
    emailid=models.EmailField(max_length=100,null=True)
    reading=models.CharField(max_length=100, default="0")
    dictation=models.CharField(max_length=100,default="0")
    match=models.CharField(max_length=100, default="0")
    comprehension=models.CharField(max_length=100,default="0")
    fill=models.CharField(max_length=100, default="0")
    count=models.CharField(max_length=100,default="0")
    currency=models.CharField(max_length=100, default="0")
    order=models.CharField(max_length=100,default="0")
    arithmetic=models.CharField(max_length=100, default="0")
    compare=models.CharField(max_length=100,default="0")
    questionnaire=models.CharField(max_length=100, default="0")
    result=models.CharField(max_length=100,default="0")

    
   
