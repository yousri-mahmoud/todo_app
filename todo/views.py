from django.shortcuts import render , redirect
from django.views.decorators.http import require_POST
from .models import  Todo
from .forms import TodoForm
# Create your views here.

def home(request):
    todo_list = Todo.objects.all()
    form = TodoForm()
    context = {'todo_list': todo_list, 'form':form }
    return render(request ,'todo/index.html' , context )

@require_POST
def add(request):
        form = TodoForm(request.POST)
        
        if form.is_valid():
            new_form = Todo(text=form.cleaned_data['text'])
            new_form.save()
            return redirect('/')

def dodo(request , todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.complet = True
    todo.save()
    return redirect('/')

def delete_text(request):
    Todo.objects.filter(complet__exact=True).delete()
    return redirect('/')



def delete_all(request):
    Todo.objects.all().delete()
    return redirect('/')