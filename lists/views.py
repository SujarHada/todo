from django.shortcuts import render , redirect, HttpResponse
from lists.models import Task
from django.views import View
from django.contrib import messages


# Create your views here.
# class Home(View):
    
class God():
 
    def index(self,request):
        tasks = Task.objects.all()
       
        return render(request,'index.html',{'tasks':tasks})


    # Add method / Post
    def add(self,request):
        if request.method=="POST":
            tname = request.POST.get('tname')
            ddate = request.POST.get('ddate')
            task = Task ()
            task.task=tname
            task.ddate = ddate
            if not task.task:
                error_message = 'Task Name required'
            elif not task.ddate:
                error_message = 'Task Date Required'
            else:

                task.save()

                return redirect("/")
            
            if error_message:
                return render(request, 'add.html', {'error_message': error_message})
            
        return render(request, 'add.html')    

   # Delete Method 
    def delete (self,request,id):
        task =Task.objects.get(ID=id)
        task.delete()

        return redirect ('/')
    

    #Edit Method / Update
    
    def edit(self ,request,id):

        if request.method=="GET":
         tasks = Task.objects.get(ID=id)
         return render(request,'edit.html',{'task':tasks})

        elif request.method=="POST":
       
            task =Task.objects.get(ID=id)
    #       tID = request.POST.get('ID')
            tname = request.POST.get('tname')
            ddate = request.POST.get('ddate')
            task.task=tname
            task.ddate = ddate
            task.save()
            return redirect("/")










# class index(View):
#     def get(self,request):
#         tasks = Task.objects.all()
#         return render(request,'index.html',{'tasks':tasks})

# class add(View):
#     def get(self,request):
#      return render(request,'add.html')  
    
#     def post(self,request):
#         if request.method=="POST":
#             tname = request.POST.get('tname')
#             ddate = request.POST.get('ddate')
#             task = Task ()
#             task.task=tname
#             task.ddate = ddate
#             if not task.task:
#                 error_message = 'Task Name required'
#             elif not task.ddate:
#                 error_message = 'Task Date Required'
#             else:

#                 task.save()

#                 return redirect("/")
            
#             if error_message:
#                 return render(request, 'add.html', {'error_message': error_message})
        

# class delete(View):

#     def get(self,request,id):
#         task =Task.objects.get(ID=id)
#         task.delete()

#         return redirect ('/')

# class edit(View):
#     def get(self ,request,id):
#         tasks = Task.objects.get(ID=id)
#         return render(request,'edit.html',{'task':tasks})

#     def post(self,request,id):
       
#         task =Task.objects.get(ID=id)
# #       tID = request.POST.get('ID')
#         tname = request.POST.get('tname')
#         ddate = request.POST.get('ddate')
#         task.task=tname
#         task.ddate = ddate
#         task.save()
#         return redirect("/")

#         return render(request,'edit.html',{'task':task})





# # class view(View):
# #     def get(self,request,id):
# #         tasks = Task.objects.get(id=id)
# #         print(tasks)
# #         return render(request, 'lists/view.html', {'tasks': tasks})    