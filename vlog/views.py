# from math import ceil
from django.shortcuts import render
from .models import *

# Create your views here.
def vlog(request):
    list=blug.objects.all()
    # tt=len(list)
    # pages=tt//2+ceil(tt/2-tt//2)                        #this line of code is logic for total pages 
    # if(sg==pages):
    #     inc=pages
    # else:
    #     inc=sg+1
    # if(sg==1):
    #     dec=1
    # else:
    #     dec=sg-1 
    params={"org":list}
    return render(request,"vlog/index.html",params)

def vlogpost(request,myid):
    vp=blug.objects.filter(bgid=myid)
    # code for next/prev button
    tp=blug.objects.all()
    total=len(tp)
    if(myid==total):
        ad=total
    else:
        ad=myid+1
    if(myid==1):
        subt=1
    else:
        subt=myid-1 

    param={"vp":vp[0],"ad":ad,"subt":subt,"total":total}
    return render(request,"vlog/vlugpost.html",param)
