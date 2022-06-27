from math import ceil
from django.shortcuts import render
from .models import *                      #you can do this as well for this line (from .models import contacts,productssignup)

# Create your views here.
def home(request):
    li=[]
    i=pt.objects.all()
    pro=pt.objects.values("category")
    c={cat["category"] for cat in pro}                                     #understand this line of code very vital
    for ct in c:
        final=pt.objects.filter(category=ct)
        li.append(final)
    dict={"lists":li}
    return render(request,"shop/index.html",dict)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    if request.method=="POST":
        naam=request.POST.get("mynam")
        em=request.POST.get("email")
        ph=request.POST.get("phone")
        queri=request.POST.get("txt")
        cnt=contt(name=naam,email=em,phone_no=ph,doubts=queri)
        cnt.save()
    return render(request,"shop/contact.html")

def pdt(request,idies):
    p=pt.objects.filter(id=idies)
    return render(request,"shop/product.html",{"pd":p[0]})

def sine(request):
    if request.method=="POST":
        eml=request.POST.get("mail")
        pw1=request.POST.get("p1")
        pw2=request.POST.get("p2")
        naam=request.POST.get("urname")
        s=signop(name=naam,email=eml,pwOne=pw1,pwTwo=pw2)
        s.save()
    return render(request,"shop/signup.html")
