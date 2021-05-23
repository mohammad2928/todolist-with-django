from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.


def index_form(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        priority = request.POST.get("priority", "")
        task = Task(name=name, priority=priority)
        task.save()
        return redirect("/")
    else:
        tasks = Task.objects.all()
        return render(request, 'myapp/index.html', {'tasks':tasks})
def delete(request, id):
    task = Task.objects.get(id=id)
    
    if request.method == "POST":
        task.delete()
        return redirect("/")
    return render(request, "myapp/delete.html")