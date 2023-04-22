from django.db import models

# Create your models here.
class School(models.Model):
    id=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=50)
    sbranch=models.CharField(max_length=50)

    def __str__(self):
        return self.sname

class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=30)


    def __str__(self):
        return self.name