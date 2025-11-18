from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from joblib import load

mymodel=load("mysite/heartrf.joblib")



def home(request):
    return render(request,"index.html")


def ourteam(request):
    return render(request,"ourteam.html")

def predict(request):
    return render(request,"predict.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def finalresult(request):
    e=request.POST['age']
    f=request.POST['sex']
    g=request.POST['cp']
    h=request.POST['trestbps']
    i=request.POST['chol']
    j=request.POST['fbs']
    k=request.POST['restecg']
    l=request.POST['thalach']
    m=request.POST['exang']
    n=request.POST['oldpeak']
    o=request.POST['slope']
    p=request.POST['ca']
    q=request.POST['thal']



    arr=[[e,f,g,h,i,j,k,l,m,n,o,p,q]]
    outp=mymodel.predict(arr)

    return render(request,"result.html",{'h':outp[0]})



def about1(request):
    e=request.POST['exp']
    inp= [[e]]
    yp=mymodel.predict(inp)
    return HttpResponse(yp)

def myui(request):
    return render(request,"ui.html")


def myapi(request):
    return JsonResponse({'djangomsg':'I am from Django Cloud'})