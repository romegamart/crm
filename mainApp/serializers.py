from rest_framework import serializers
from .models import *
class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100,)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=10,)
    password=serializers.CharField(max_length=30,)
    address=serializers.CharField(max_length=200,)
    empstatus=serializers.CharField(max_length=30)
    date=serializers.CharField(max_length=50)
    def create(self, validatedData):
        return Employee.objects.create(**validatedData)
    

class ClientSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    username=serializers.CharField(max_length=100)
    clinet_type=serializers.CharField(max_length=100)
    client_name=serializers.CharField(max_length=100)
    client_phone=serializers.CharField(max_length=10)
    client_email=serializers.EmailField()
    client_address=serializers.CharField(max_length=300)
    client_status=serializers.CharField(max_length=100)
    client_next_followup_date=serializers.CharField(max_length=30)
    created_on=serializers.CharField(max_length=100)
    updated_on=serializers.CharField(max_length=100)
    def create(self, validatedData):
        return Client.objects.create(**validatedData)
     

class Client_HistorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    client_phone=serializers.CharField(max_length=10)
    client_next_followup_date=serializers.CharField(max_length=30)
    client_message=serializers.CharField(max_length=None)
    updated_on=serializers.CharField(max_length=100)
    def create(self, validatedData):
        return Client_History.objects.create(**validatedData)
    