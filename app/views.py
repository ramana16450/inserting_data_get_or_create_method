from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)
def display_web(request):
    WTO=webpage.objects.all()
    d={'WTO':WTO}
    return render(request,'display_web.html',d)
def display_ar(request):
    ATO=Accessrecords.objects.all()
    d={'ATO':ATO}
    return render(request,'display_ar.html',d)