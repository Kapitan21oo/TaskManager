from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from task_app.models import Task
from task_app.form import TaskForm, TaskEditForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

@login_required
def index(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        'all_task': data_task,
    }
    return render(request, 'task_app/index.html', context=context)

@login_required
def create_task(request):
    redirect = reverse('index')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            res = Task(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                user=request.user
            )
            res.save()
            return HttpResponseRedirect(redirect)
    else:
        form = TaskForm()
    return render(request, 'task_app/create_task.html', {'form': form})




@login_required
def delete_task(request, id_task):
    redirect = reverse('index')
    if request.method == 'POST':
        res = Task.objects.get(id=id_task)
        res.delete()
        return HttpResponseRedirect(redirect)
    else:
        return render(request, 'task_app/delete_task.html')




@login_required
def edit_task(request, id_task):
    redirect = reverse('index')
    context = {
        'form': TaskEditForm
    }
    if request.method == 'POST':
        form = TaskEditForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # task = Task.objects.get(id=id_task)
            task = Task(
                id=id_task,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                user = request.user
            )
            task.save()
            return HttpResponseRedirect(redirect)

    return render(request, 'task_app/edit_task.html', context=context)
