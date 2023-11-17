from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.gis.db import models
from django.shortcuts import get_object_or_404, redirect

from . import models
from .forms import ProjectForm, CustomMapsForm, PinsForm, IconsForm
from .models import Project, CustomMaps
from .functions import handle_uploaded_project_file
from zipfile import ZipFile

# Create your views here.
def index_page(request):
    context = {}
    return render(request, 'index.html', context=context)

def custommaps(request):
    maps = CustomMaps.objects.all()
    context = { 'custom_maps' : maps}
    return render(request, 'custommaps.html', context)

def custommaps_detail(request, title):
    try:
        custom_map = CustomMaps.objects.get(title=title)
        print(custom_map.tiles_folder)
        context = { 'custom_map' : custom_map }
        return render(request, 'custom_map_detail.html', context)
    except CustomMaps.DoesNotExist:
        return render(request, '404.html')

def create_custommaps(request):
    if request.method == "GET":
        form = CustomMapsForm()

        return render(request, 'create_custommap.html', context={'form':form})
    
    if request.method == "POST":
        print("Uploading data")
        form = CustomMapsForm(request.POST, request.FILES)
        if form.is_valid():
            fileUrl = handle_uploaded_project_file(request.FILES["tiles"], request.POST['title'])
            print(fileUrl)

            if fileUrl:
                custommaps_instance = form.save(commit=False)
                custommaps_instance.tiles_folder = fileUrl
                custommaps_instance.save()
                
                return JsonResponse({'data':'Data uploaded'})
            else:
                return JsonResponse({'data':'Something went wrong!!'})
            
        else:
            print(form.errors)
            return JsonResponse({'data':'Something went wrong!!'})

def pins_page(request):
    context = {}
    return render(request, 'pins.html', context=context)


def projects(request):
    projects = Project.objects.all()
    context = { 'projects' : projects }
    return render(request, 'projects.html', context)


def create_project(request):
    if request.method == "GET":
        form = ProjectForm()

        return render(request, 'project.html', context={'form':form})
    
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()               
            return redirect("/projects/")
        else:
            return render(request, 'project.html', context={'form':form})

def project_detail(request, title):
    try:
        pinsForm = PinsForm()
        map_project = Project.objects.get(title=title)
        # custom_map = CustomMaps.objects.get()
        context = { 'project' : map_project, 'pinsForm':pinsForm, 'custom_map' : map_project.custom_map }
        return render(request, 'project_detail.html', context)
    except Project.DoesNotExist:
        return render(request, '404.html')


# export projects to a downloadable html file

    

    
