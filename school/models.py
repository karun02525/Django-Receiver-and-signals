from django.db import models
from datetime import datetime   
from .managers import CustomManager 
import uuid
from django.contrib.auth.models import User




class Page(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE , primary_key=True)
    #user = models.ForeignKey(User,on_delete=models.CASCADE , primary_key=True)
    #user = models.OneToOneField(User,on_delete=models.CASCADE , primary_key=True, limit_choices_to={'is_staff':True})
    #user = models.OneToOneField(User,on_delete=models.PROTECT , primary_key=True)
    name = models.CharField(max_length=30)
    date = models.DateField()











class BaseModel(models.Model):
    base_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class ExamCenter(BaseModel):
    base_id= None
    cname = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    
class Student(ExamCenter):
    base_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    roll = models.IntegerField()   
    
    
class ProxyStudent(Student):
    str=CustomManager() 
    class Meta:
       proxy=True
       ordering=['name']



class Teacher(BaseModel):
    base_id= None
    teacher_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    