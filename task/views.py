from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from task.models import Tarefa

@login_required
def index(request):
    return render(request, 'task/index.html')

@login_required
def task_list(request):
    lista = Tarefa.objects.all()
    return render(request, 'task/tasks.html', {'tarefas': lista})

@login_required
def create(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data =request.POST.get('data')
        status = False
        Tarefa.objects.create(tarefa=titulo, descricao=descricao, data=data, status=status)
        return redirect('index')
    return render(request, 'task/create.html')

@login_required
def delete_task(request, id):
    tarefa = Tarefa.objects.get(pk=id)

    if request.method == 'POST':
        tarefa.delete()
        return redirect('index')

    return render(request, 'task/delete_task.html', {'tarefa': tarefa})
   
@login_required
def edit_task(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.data = request.POST.get('data')
        tarefa.status = 'status' in request.POST
        tarefa.save()
        return redirect('index')        
    return redirect('index')
        
