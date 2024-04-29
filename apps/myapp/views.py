from django.shortcuts import redirect,render,HttpResponse
from rest_framework import viewsets
from .models import AndroidApp, Task, TaskCompletion, UserProfile, AdminProfile
from .serializers import AndroidAppSerializer, TaskSerializer, TaskCompletionSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
class AndroidAppViewSet(viewsets.ModelViewSet):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCompletionViewSet(viewsets.ModelViewSet):
    queryset = TaskCompletion.objects.all()
    serializer_class = TaskCompletionSerializer

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('profile')  # Redirect to profile page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def profile(request):
    user = request.user
    # Assuming you have a UserProfile model linked to the user
    profile = UserProfile  # Replace 'profile' with the name of your profile model
    return render(request, 'profile.html', {'user': user, 'profile': profile})

def adminsignup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def adminlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('adminprofile')  # Redirect to profile page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def adminprofile(request):
    user = request.user
    # Assuming you have a UserProfile model linked to the user
    profile = AdminProfile  # Replace 'profile' with the name of your profile model
    return render(request, 'adminprofile.html', {'user': user, 'profile': profile})
