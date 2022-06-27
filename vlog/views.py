from django.shortcuts import render
from .models import *

# Create your views here.
def vlog(request):
    list=blug.objects.all()
    params={"org":list}
    return render(request,"vlog/index.html",params)

def vlogpost(request,myid):
    vp=blug.objects.filter(bgid=myid)
    param={"vp":vp[0]}
    return render(request,"vlog/vlugpost.html",param)
