from django.shortcuts import render , redirect, HttpResponse
from lists.models import Task
from django.views import View

# Create your views here.
class index(View):
    def get(self,request):
        tasks = Task.objects.all()
        return render(request,'index.html',{'tasks':tasks})

class add(View):
    def get(self,request):
     return render(request,'add.html')  
    
    def post(self,request):
        if request.method=="POST":
            tname = request.POST.get('tname')
            ddate = request.POST.get('ddate')
            task = Task ()
            task.task=tname
            task.ddate = ddate
            task.save()
            return redirect("/")
        

class delete(View):

    def get(self,request,id):
        task =Task.objects.get(ID=id)
        task.delete()

        return redirect ('/')

class edit(View):
    def get(self ,request,id):
        tasks = Task.objects.get(id=id)
        

    def post(request,id):
        # task =Task.objects.get(ID=id)
        if request.method=="POST":
        #    tID = request.POST.get('ID')
           tname = request.POST.get('tname')
           ddate = request.POST.get('ddate')
           task = Task ( task=tname , ddate = ddate)
           task.save()
           return render(request,'index.html')
    

        return render(request,'edit.html',{'task':task})

class edit_it(View):
    def get(request,id):
    
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

class view(View):
    def get(self,request,id):
        tasks = Task.objects.get(id=id)
        print(tasks)
        return render(request, 'lists/view.html', {'tasks': tasks})    