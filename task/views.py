from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def task_all(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task/task_all.html', context)


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            completed = form.cleaned_data['completed']
            task = Task.objects.create(title=title, description=description, completed=completed)
            return redirect('task_all')
    else:
        form = TaskForm()
    return render(request, 'task/task_add.html', {'form': form})
