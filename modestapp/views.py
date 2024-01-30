from django.shortcuts import render
from . models import Places
from . models import Team
# Create your views here.
def home(request):
    places=Places.objects.all()
    team=Team.objects.all()
    return render(request,'index.html',{'result1':places,'result2':team})

