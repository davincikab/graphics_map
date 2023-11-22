from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.gis.db import models
from django.shortcuts import get_object_or_404, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . import models
from .forms import ProjectForm, CustomMapsForm, PinsForm, IconsForm
from .models import Project, CustomMaps, Icons, Pins
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
        # print(custom_map.tiles_folder)
        context = { 'custom_map' : custom_map }
        return render(request, 'custom_map_detail.html', context)
    except CustomMaps.DoesNotExist:
        return render(request, '404.html')

@login_required
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

@login_required
def create_project(request):
    if request.method == "GET":
        form = ProjectForm()

        return render(request, 'project.html', context={'form':form})
    
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()               
            # return JsonResponse({"data":"Success"})
            return redirect("/projects")
        else:
            return render(request, 'project.html', context={'form':form})

def project_detail(request, title):
    try:
        pinsForm = PinsForm()
        map_project = Project.objects.get(title=title)
        pins_icons = Icons.objects.exclude(icon_type="Accesibility")
        acc_icons = Icons.objects.filter(icon_type="Accesibility")
        # custom_map = CustomMaps.objects.get()
        context = { 
            'project' : map_project, 
            'pinsForm':pinsForm, 
            'custom_map' : map_project.custom_map,
            "pins_icons":pins_icons, 
            "accessebility_icons":acc_icons,
            "user":request.user
        }
        return render(request, 'project_detail.html', context)
    except Project.DoesNotExist:
        return render(request, '404.html')

# pins cruds
def create_pins(request):
    if request.method == 'POST':
        form = PinsForm(request.POST, request.FILES)
        project = Project.objects.get(pk=request.POST.get('project'))

        poi_type = request.POST.get('poi_type')

        if poi_type == 'Area Pin':
            minzoom = project.custom_map.minzoom
            maxzoom = project.custom_map.minzoom + 2
        else:
            minzoom = project.custom_map.minzoom + 2
            maxzoom = project.custom_map.maxzoom 

        
        if form.is_valid():
            # 'minzoom', 'maxzoom', 
            pin_instance = form.save(commit=False)
            pin_instance.icon = request.POST.get('icon')
            pin_instance.project = project
            pin_instance.poi_category =  request.POST.get('poi_type')
            pin_instance.latitude = request.POST.get('latitude')
            pin_instance.longitude = request.POST.get('longitude')
            pin_instance.accesibility_features = request.POST.get('accesibility_features')
            pin_instance.minzoom = minzoom
            pin_instance.maxzoom = maxzoom


            pin_instance.save()
            return JsonResponse({'data':'Success!!'})
        else:
            return JsonResponse({'data':'Failed!'})

def delete_pins(request, title):
    if request.method == 'DELETE':
        try:
            pin = Pins.objects.get(title=title)
            pin.delete()

            return JsonResponse({'data':'Success!'})
        except Pins.DoesNotExist:
            return JsonResponse({'data':'Something went wrong!!'})    

def get_pins(request):
    projectId =request.GET['project_id']
    if projectId:
        project = Project.objects.get(pk=projectId)
        pins = Pins.objects.filter(project=project)
    else:
        pins = Pins.objects.all()
    pins_json = serializers.serialize('json', pins)

    # print(pins_json)
    return JsonResponse({'data':pins_json})

# icons section
@login_required
def icons_list(request):
    if request.method == 'GET':

        pins_icons = Icons.objects.filter(icon_type="Pin")
        acc_icons = Icons.objects.filter(icon_type="Accesibility")
        area_icons = Icons.objects.filter(icon_type="Area")
        form = IconsForm()
        
        context = {
            "area_icons":area_icons,
            "pins_icons":pins_icons, 
            "accessebility_icons":acc_icons, 
            "form":form
        }

        return render(request, "icons.html", context)

    if request.method == 'POST':
        form = IconsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return JsonResponse({'data':'Success!'})
        else:
            # print(form.errors)
            return JsonResponse({'data':'Something went wrong!!'})    
    

def get_icons(request):
    icons = Icons.objects.all()
    return JsonResponse({'data':icons})
# export projects to a downloadable html file

    

    
# user
def logout_view(request):
    logout(request)
    
    return redirect