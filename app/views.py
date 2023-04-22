from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.

def School_Form(request):
    TF=SchoolForm()
    d={'TF':TF}
    if request.method=='POST':
        SFD=SchoolForm(request.POST)
        if SFD.is_valid():
            id=SFD.cleaned_data['id']
            sname=SFD.cleaned_data['sname']
            sbranch=SFD.cleaned_data['sbranch']
            So=School.objects.get_or_create(id=id,sname=sname,sbranch=sbranch)[0]
            So.save()
            return HttpResponse('Data inserted successfully')
    return render(request,'School_Form.html',d)

def Student_Form(request):
    WF=StudentForm()
    d={'WF':WF}
    if request.method=='POST':
        SFS=StudentForm(request.POST)
        if SFS.is_valid():
            id=SFS.cleaned_data['id']
            name=SFS.cleaned_data['name']
            age=SFS.cleaned_data['age']
            gender=SFS.cleaned_data['gender']
            St=Student.objects.get_or_create(id=id,name=name,age=age,gender=gender)[0]
            St.save()
            return HttpResponse('Student data inserted')
    return render(request,'Student_Form.html',d)