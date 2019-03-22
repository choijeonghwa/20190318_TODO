from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User
from .forms import TodoForm



# Create your views here.
def home(request):
    # todos에 있는 내용을 다 가져와 보여주기
    # todos = Todo.objects.all().order_by('-id')
    # todos = Todo.objects.filter(user_id=request.user.id).all()
    # todos = request.user.todo_set.all()
    # todos = request.user.todos

    if request.user.is_authenticated:
        todos = request.user.todo_set.all()
        content = {
            'todos': todos
        }
    else:
        content = {}
    return render(request, 'todos/home.html', content)


def create(request):
    # todos 작성하기
    # content = request.POST.get('content')
    # user_id = request.user.id

    user = request.user
    todo = Todo(user=user)
    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
        form.save()

    # user_id = User.objects.first().id
    # complete = request.POST.get('completed')
    # Todo.objects.create(content=content, user_id=user_id)

    return redirect('todos:home')


def check(request, id):
    # 특정 id를 가진 todo를 뽑아 completed = True
    todo = Todo.objects.get(pk=id)
    todo.completed = False if todo.completed else True
    todo.save()
    return redirect('todos:home')
