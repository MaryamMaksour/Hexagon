from .forms import CreateUserForm, ProjectForm, ProjectForm2
from .models import Project, Project2, questions
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .generate import generate_string

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def form_page(request):
            
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  
            project.save()
            return redirect('form')
    else:
        form = ProjectForm()
    return render(request, 'form2.html', {'form': form})

@login_required
def form_page2(request):
            
    if request.method == 'POST':
        form = ProjectForm2(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  
            project.save()
            return redirect('result')
    else:
        form = ProjectForm2()
    
    question = questions.objects.all()
    return render(request, 'form.html', {'form': form, 'questions': question })


@login_required
def result_page(request):
    last_project = Project.objects.filter(user=request.user).last()
    last_project2 = Project2.objects.filter(user=request.user).last()
    
    my_string = generate_string(last_project, last_project2)
    
    return render(request, 'result.html',{'my_string': my_string})


   
