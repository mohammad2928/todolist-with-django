from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index_form(request):
    """
    main page
    a list of tasks
    """
    if request.method == "POST":
         # check done form
        done_id = request.POST.get("done", "")
        if done_id:
            task = Task.objects.filter(id=done_id)
            if task[0].status == 1:
                task.update(status=0)
            else:
                task.update(status=1)
            return redirect("/")

        # check filter
        filter = request.POST.get("filter", "")
        
        if filter == "end_date":
            tasks = Task.objects.order_by('end_date')
            return render(request, 'myapp/index.html', {'tasks':tasks})
        elif filter == "start_data":
            tasks = Task.objects.order_by('name')
            return render(request, 'myapp/index.html', {'tasks':tasks})
        elif filter == "priority":
            tasks = Task.objects.order_by('priority')
            return render(request, 'myapp/index.html', {'tasks':tasks})
        elif filter == "dones":
            tasks = Task.objects.filter(status=1)
            return render(request, 'myapp/index.html', {'tasks':tasks})
        elif filter == "remains":
            tasks = Task.objects.filter(status=0)
            return render(request, 'myapp/index.html', {'tasks':tasks})
        else:
            tasks = Task.objects.order_by('id')
            return render(request, 'myapp/index.html', {'tasks':tasks})
    else:
        tasks = Task.objects.all()
        return render(request, 'myapp/index.html', {'tasks':tasks})

def delete(request, id):
    """
    remove a task by id
    
    """

    task = Task.objects.filter(id=id)
    if request.method == "POST":
        task.update(status=1)
        return redirect("/")
    return render(request, "myapp/delete.html")

def add_task(request):
    """
    create a task
    
    """
    if request.method == "POST":
        name = request.POST.get("name","")
        priority = request.POST.get("priority", "")
        end_date = request.POST.get("end_date", "")
        description = request.POST.get("description", "")
        task = Task(name=name, priority=priority, description=description, end_date=end_date)
        task.save()
        return redirect("/")
    else:
        return render(request, "myapp/add.html")