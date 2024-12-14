from django.db import models

# Create your models here.

class Client(models.Model):
    id=models.AutoField(primary_key=True)
    emp_name=models.CharField(max_length=100,default='',null=True,blank=True)
    username=models.CharField(max_length=100,default='',null=True,blank=True)
    clinet_type=models.CharField(max_length=100,default='',null=True,blank=True)
    client_name=models.CharField(max_length=100,default='',null=True,blank=True)
    client_phone=models.CharField(max_length=10)
    client_email=models.EmailField(default='',null=True,blank=True)
    client_address=models.CharField(max_length=300,default='',null=True,blank=True)
    client_next_followup_date=models.CharField(max_length=30,default='')
    client_status=models.CharField(max_length=100,default="pending",null=True,blank=True)
    created_on=models.CharField(max_length=100,default='',null=True,blank=True)
    updated_on=models.CharField(max_length=100,default='',null=True,blank=True)
    allocator=models.CharField(max_length=100,default='',null=True,blank=True)
    def __str__(self):
        return str(self.client_name)
    
    
class Client_History(models.Model):
    id=models.AutoField(primary_key=True)
    client_phone=models.CharField(max_length=10)
    client_next_followup_date=models.CharField(max_length=30,default='')
    client_message=models.TextField(default='',null=True,blank=True)
    updated_on=models.CharField(max_length=100,default='',null=True,blank=True)
    def __str__(self):
        return str(self.client_phone)
    
    
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=30,default='Telesales',null=True,blank=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    email=models.EmailField(default='',null=True,blank=True)
    phone=models.CharField(max_length=10,default='',null=True,blank=True)
    password=models.CharField(max_length=30,default='',null=True,blank=True)
    address=models.CharField(max_length=200,default='',null=True,blank=True)
    empstatus=models.CharField(max_length=30,default='active',null=True,blank=True)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.name 
    


class Image(models.Model):
    id=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="image")



class Email_Data(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,default='')
    email=models.EmailField()
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.email)