from django.shortcuts import render , redirect, HttpResponse
from lists.models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()

    
    return render(request,'index.html',{'tasks':tasks})

def add(request):
    # if request.method=="POST":
    #    tname = request.POST.get('tname')
    #    ddate = request.POST.get('ddate')
    #    task = Task ()
    #    task.task=tname
    #    task.ddate = ddate
    #    task.save()

    return render(request,'add.html')

def delete(request,id):
    task =Task.objects.get(ID=id)
    task.delete()

    return redirect ('/')

def edit(request,id):
    task =Task.objects.get(ID=id)
    # if request.method=="POST":
    # #    tID = request.POST.get('ID')
    #    tname = request.POST.get('tname')
    #    ddate = request.POST.get('ddate')
    #    task = Task ( task=tname , ddate = ddate)
    #    task.save()
    #    return render(request,'index.html')
    

    return render(request,'edit.html',{'task':task})


def edit_it(request,id):
    
    if request.method=="POST":
       task =Task.objects.get(ID=id)
    #    tID = request.POST.get('ID')
       tname = request.POST.get('tname')
       ddate = request.POST.get('ddate')
       task.task=tname
       task.ddate = ddate
       task.save()
       return redirect("/")
    

    # return render(request,'edit.html',{'task':task})