from django.shortcuts import render,redirect, HttpResponse


def index_view(request):
    return render(request,'index.html')


def index_view(request):
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'contact.html')

def cv_view(request):
    return render(request, 'cv.html')

def resume_view(request):
    return render(request, 'resume.html')

def projects_view(request):
    return render(request, 'projects.html')