from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ToDoForm
from .models import ToDo


def index(request):
    todos = ToDo.objects.select_related('author').all()
    return render(request, "todos/index.html", {"todos": todos})


@login_required
def add(request):
    form = ToDoForm(request.POST or None)
    if request.method != "POST":
        return render(request, "todos/add.html", {"form": form})
    if not form.is_valid():
        return render(request, "todos/add.html", {"form": form})
    todo = form.save(commit=False)
    todo.author = request.user
    todo.save()
    return redirect("todos:index")