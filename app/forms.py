from django import forms
from app.models import *

g=[('Male','Male'),('Female','Female')]

class SchoolForm(forms.Form):
    id=forms.IntegerField()
    sname=forms.CharField(max_length=50)
    sbranch=forms.CharField(max_length=50)


class StudentForm(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
