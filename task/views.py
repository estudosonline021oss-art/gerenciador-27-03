from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from task.models import Tarefa
from .forms import TarefaForm

@login_required
def index(request):    
    return render(request, 'task/index.html')

@login_required
def task_list(request):
    lista = Tarefa.objects.filter(usuario = request.user)
    return render(request, 'task/tasks.html', {'tarefas': lista})

@login_required
def create(request):
    form = TarefaForm(request.POST or None)
    if request.method == 'POST'and form.is_valid():
        tarefa = form.save(commit=False)
        tarefa.usuario = request.user
        tarefa.save()
        return redirect('index')
    return render(request, 'task/create.html', {'form': form})

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
        
