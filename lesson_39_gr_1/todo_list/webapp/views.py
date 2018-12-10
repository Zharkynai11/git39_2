from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def index_view(request):
    return render(request, 'index.html', context={
        'tasks': Task.objects.all()
    })


def create_task_view(request):

    task = Task.objects.create(
        name=request.POST.get('task_name')
    )
    return redirect('task_index')


def delete_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'task_delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('task_index')

def complete_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.status = "done"
    task.save()
    return redirect('task_index')

def delete_all_view(request):
    for task in filter(lambda task: task.status=="done", Task.objects.all()):
        task.delete()
    return redirect('task_index')