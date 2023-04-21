from django.shortcuts import render
from app.forms import *
# Create your views here.

def Topic_Form(request):
    TF=TopicForm()
    d={'TF':TF}
    return render(request,'Topic_Form.html',d)

def Webpage_Form(request):
    WF=WebpageForm()
    d={'WF':WF}
    return render(request,'Webpage_Form.html',d)