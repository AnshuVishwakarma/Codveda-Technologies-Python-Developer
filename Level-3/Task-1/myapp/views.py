from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CustomUserCreationForm, TaskForm
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.
def home(request):
    return render(request,'index.html')
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')

        # Check if username already exists
        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        # Create user
        user = User.objects.create_user(
            username=name,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'register.html')

from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')

        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return redirect('login')

# @login_required
# def dashboard(request):
#     if request.user.is_staff:
#         role = "Admin"
#     else:
#         role = "Regular User"

#     return render(request, 'dashboard.html', {'role': role})

@login_required
def dashboard(request):
    if request.user.is_staff:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {'tasks': tasks})

# Example Admin-Only View
# @login_required
# def delete_task(request):
#     if not request.user.is_staff:
#         return HttpResponse("Access Denied")

#     return HttpResponse("Task Deleted Successfully")
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if not request.user.is_staff and task.user != request.user:
        return redirect('dashboard')

    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'update_task.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if not request.user.is_staff and task.user != request.user:
        return redirect('dashboard')

    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')

    return render(request, 'delete_task.html', {'task': task})