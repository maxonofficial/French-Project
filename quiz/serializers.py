from rest_framework import serializers
from  . import models

class Department(serializers.ModelSerializer):
    class Meta:
        model = models.department
        exclude = ['created_at','updated_at']

class Word(serializers.ModelSerializer):
    department = Department()
    class Meta:
        model = models.word
        exclude = ['created_at','updated_at']


