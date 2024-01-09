from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.core import serializers
import json
import os
import requests
import shutil
from pathlib import Path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import ProjectForm, CustomMapsForm, PinsForm, IconsForm, PinCategoryForm, PinSubCategoryForm
from .models import Project, CustomMaps, Icons, Pins, PinSubCategory, PinCategory
from .functions import handle_uploaded_project_file, zip_directory, unzip_to_dir, delete_zip, move_accessibility_icons
from zipfile import ZipFile

from django.utils import translation
from django.db.models import Q
from django.conf import settings

# Create your views here.
def index_page(request):
    context = {}
    return render(request, 'index.html', context=context)

@login_required
def custommaps(request):
    if request.user.is_superuser:
        maps = CustomMaps.objects.all()
    
        context = { 'custom_maps' : maps}
        return render(request, 'custommaps.html', context)
    else:
        return render(request, '404.html')

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
            
            if request.POST.get('is_osm_based_map') != "on":
                fileUrl = handle_uploaded_project_file(request.FILES["tiles"], request.POST['title'])
            else:
                fileUrl = "osm_map"
            print("Center: ", request.POST.get('center'))

            if fileUrl:
                custommaps_instance = form.save(commit=False)
                custommaps_instance.tiles_folder = fileUrl
                custommaps_instance.center = request.POST.get('center')
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

@login_required
def projects(request):
    print("Projects Page")
    print(translation.get_language_from_request(request=request))
    if request.user.is_superuser:
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(project_owner=request.user)
    context = { 'projects' : projects }
    return render(request, 'projects.html', context)

@login_required
def create_project(request):
    if request.user.is_superuser == False:
        return redirect("/projects")
    
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

@login_required
def project_detail(request, title):
    try:
        pinsForm = PinsForm()
        map_project = Project.objects.get(Q(title=title) | Q(title_ar=title) | Q(title_he=title) | Q(title_en=title))
        print(request.user.is_superuser)
        if request.user.is_superuser == False:
            if request.user != map_project.project_owner:
                return render(request, "not-authorized.html")
        pins_icons = Icons.objects.exclude(icon_type="Accesibility")
        acc_icons = Icons.objects.filter(icon_type="Accesibility")
        project_categories = PinCategory.objects.filter(project=map_project).filter(is_simple_icon=False).filter(is_area_category=False).order_by('ranking_value')
        pin_categories = PinCategory.objects.filter(project=map_project)
        # custom_map = CustomMaps.objects.get()

        print(project_categories)
        context = { 
            'project' : map_project, 
            'pinsForm':pinsForm, 
            'custom_map' : map_project.custom_map,
            "pins_icons":pins_icons, 
            "accessebility_icons":acc_icons,
            "user":request.user,
            "pin_categories":pin_categories,
            "categories":project_categories
        }
        return render(request, 'project_detail.html', context)
    except Project.DoesNotExist:
        return render(request, '404.html')

# export projects to a downloadable html file
def project_view(request, title):
    print(title)
    try:
        map_project = Project.objects.get(Q(title=title) | Q(title_ar=title) | Q(title_he=title) | Q(title_en=title))
        pins_icons = Icons.objects.exclude(icon_type="Accesibility")
        acc_icons = Icons.objects.filter(icon_type="Accesibility")
        project_categories = PinCategory.objects.filter(project=map_project).filter(is_simple_icon=False).filter(is_area_category=False).order_by('ranking_value')
        
        if request.GET.get('lang'):
            translation.activate(request.GET.get('lang'))
            # request.session['django_language'] = map_project.project_language
        else:
           translation.activate(map_project.project_language)

        context = { 
            'project' : map_project, 
            'custom_map' : map_project.custom_map,
            "pins_icons":pins_icons, 
            "accessebility_icons":acc_icons,
            "user":request.user,
            "categories":project_categories
        }
        
        return render(request, 'project_export.html', context)
    except Project.DoesNotExist:
        return render(request, '404.html')

def project_view_export(request, title):
    print(title)
    try:
        map_project = Project.objects.get(Q(title=title) | Q(title_ar=title) | Q(title_he=title) | Q(title_en=title))
        pins_icons = Icons.objects.exclude(icon_type="Accesibility")
        acc_icons = Icons.objects.filter(icon_type="Accesibility")
        project_categories = PinCategory.objects.filter(project=map_project).filter(is_simple_icon=False).filter(is_area_category=False).order_by('ranking_value')
        
        if request.GET.get('lang'):
            translation.activate(request.GET.get('lang'))
        else:
            translation.activate(map_project.project_language)

        context = { 
            'project' : map_project, 
            'custom_map' : map_project.custom_map,
            "pins_icons":pins_icons, 
            "accessebility_icons":acc_icons,
            "user":request.user,
            "categories":project_categories
        }
        
        return render(request, 'project_local.html', context)
    except Project.DoesNotExist:
        return render(request, '404.html') 
# pins cruds
def create_pins(request):
    if request.method == 'POST':
        form = PinsForm(request.POST, request.FILES)
        project = Project.objects.get(pk=request.POST.get('project'))
        poi_type = request.POST.get('poi_type')
        pin_type = request.POST.get('pin_type')
        print(pin_type)

        try:
            pin_category = PinCategory.objects.get(Q(title=request.POST.get("category")) & Q(project=project))
        except PinCategory.DoesNotExist:
            pin_category = PinCategory(title=pin_type, title_en="", title_he="", title_ar="")

        # if pin_type == "Simple Icon" or pin_type == "Simple Text":
        #     pin_category = PinCategory(title=pin_type, title_en="", title_he="", title_ar="")
        #     # {"title":pin_type, "title_en":"", "title_he":"", "title_ar":""}
        # else:
        #     pin_category = PinCategory.objects.get(Q(title=request.POST.get("category")) & Q(project=project))

        

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
            pin_instance.category = pin_category.title

            pin_instance.category_en = pin_category.title_en
            pin_instance.category_ar = pin_category.title_ar
            pin_instance.category_he = pin_category.title_he
            
            if request.POST.get('subcategory'):
                subcategory_title = request.POST.get('subcategory')
                subcategory = PinSubCategory.objects.get(
                    Q(title=subcategory_title) | Q(title_en=subcategory_title) | Q(title_he=subcategory_title) |
                    Q(title_ar=subcategory_title) 
                )
                pin_instance.subcategory = subcategory.title
                pin_instance.subcategory_en = subcategory.title_en
                pin_instance.subcategory_ar = subcategory.title_ar
                pin_instance.subcategory_he = subcategory.title_he

            pin_instance.icon = pin_category.icon
            pin_instance.active_icon = pin_category.active_icon
            pin_instance.latitude = request.POST.get('latitude')
            pin_instance.longitude = request.POST.get('longitude')
            pin_instance.accesibility_features = request.POST.get('accesibility_features')
            pin_instance.minzoom = minzoom
            pin_instance.maxzoom = maxzoom


            pin_instance.save()
            return JsonResponse({'data':'Success!!'})
        else:
            return JsonResponse({'data':'Failed!'})

def update_pin_details(request, pin_pk):
    if request.method == "POST":
        pin = Pins.objects.get(pk=pin_pk)
        form =PinsForm(request.POST, request.FILES, instance=pin)
        project = Project.objects.get(pk=request.POST.get('project'))
        pin_category = PinCategory.objects.get(Q(title=request.POST.get("category")) & Q(project=project))

        if form.is_valid():
            pin_instance = form.save(commit=False)
            pin_instance.accesibility_features = request.POST.get('accesibility_features')

            # update category values
            pin_instance.icon = pin_category.icon
            pin_instance.active_icon = pin_category.active_icon
            pin_instance.category_en = pin_category.title_en
            pin_instance.category_ar = pin_category.title_ar
            pin_instance.category_he = pin_category.title_he

            if request.POST.get('subcategory'):
                subcategory_title = request.POST.get('subcategory')
                subcategory = PinSubCategory.objects.get(
                    Q(title=subcategory_title) | Q(title_en=subcategory_title) | Q(title_he=subcategory_title) |
                    Q(title_ar=subcategory_title) 
                )
                pin_instance.subcategory = subcategory.title
                pin_instance.subcategory_en = subcategory.title_en
                pin_instance.subcategory_ar = subcategory.title_ar
                pin_instance.subcategory_he = subcategory.title_he
            else:
                pin_instance.subcategory = ""
                pin_instance.subcategory_en = ""
                pin_instance.subcategory_ar = ""
                pin_instance.subcategory_he = ""

            pin_instance.latitude = request.POST['latitude']
            pin_instance.longitude = request.POST['longitude']
            # pin.title = request.POST['title']
            # pin.subtitle = request.POST['subtitle']
            # pin.description = request.POST['description']
            # pin.description = request.POST['description']

            pin_instance.save()
            return JsonResponse({'data':'Success!!'})
        else:
            return JsonResponse({'data':'Failed!'})
    else:
        return JsonResponse({'data':'Failed!'})
def delete_pins(request, pin_pk):
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


# categories and sub categories
def project_categories(request, title):
    print(title)
    if request.method == 'GET':
        try:
            project = Project.objects.get(Q(title=title) | Q(title_ar=title) | Q(title_he=title) | Q(title_en=title))
            pin_categories = PinCategory.objects.filter(project=project.pk).select_related()

            categoryForm = PinCategoryForm()
            subCategoryForm = PinSubCategoryForm()

            # print(pin_categories[0].pinsubcategory_set.all())
            context = {
                "categories":pin_categories,
                "sub_category_form":subCategoryForm,
                "category_form":categoryForm
            }

            return render(request, "project_categories.html", context)

        except Project.DoesNotExist:
            return render(request, '404.html')

    if request.method == 'POST':
        form = IconsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return JsonResponse({'data':'Success!'})
        else:
            # print(form.errors)
            return JsonResponse({'data':'Something went wrong!!'}) 

# add a category
def add_category(request):
    if request.method == 'POST':
        form = PinCategoryForm(request.POST, request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.title = request.POST['title']
            category.title_en = request.POST['title']
            category.title_ar = request.POST['title']
            category.title_he = request.POST['title']

            category.save()
            return JsonResponse({'data':'Success!'})
        else:
            print(form.errors)
            return JsonResponse({'data':'Something went wrong!!'})

# add a category
def add_sub_category(request):
    if request.method == 'POST':
        form = PinSubCategoryForm(request.POST)

        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.title = request.POST['title']
            subcategory.title_en = request.POST['title']
            subcategory.title_ar = request.POST['title']
            subcategory.title_he = request.POST['title']

            subcategory.save()

            return JsonResponse({'data':'Success!'})
        else:
            # print(form.errors)
            return JsonResponse({'data':'Something went wrong!!'}) 

def get_categories(request):
    projectId =request.GET['project_id']
    if projectId:
        project = Project.objects.get(pk=projectId)
        categories = PinCategory.objects.filter(project=project).prefetch_related('pinsubcategory_set')
    else:
        categories = Pins.objects.all().prefetch_related('pinsubcategory_set')

    categoriesDict = {}
    for e in categories:
        subcategories = [l.title for l in e.pinsubcategory_set.all()]
        categoriesDict[e.title] = subcategories
        
    print(categoriesDict)
    pins_json = json.dumps(categoriesDict)

    # print(pins_json)
    return JsonResponse({'data':pins_json})
   
def export_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    pins = Pins.objects.filter(project=project)
    media_root_dir = settings.MEDIA_ROOT
    static_files_root_dir = settings.STATIC_ROOT

    # get the pins json data
    pins_json = serializers.serialize('json', pins)
    path = f"{media_root_dir}/export/{project.title}"    
    ssh = Path(path)

    if not os.path.exists(path):
        ssh.mkdir(parents=True)
    with open(f'{path}/data.json', 'w+', encoding='utf-8') as f:
        f.write(pins_json)
        # json.dump(pins_json, f, ensure_ascii=False, indent=4)
    

    # get all the icons a zip file
    icons_path = f"{media_root_dir}/uploads/icons/{project.title}"
    zip_directory(icons_path, f'{media_root_dir}/export/{project.title}/icons.zip')
    unzip_to_dir(f'{media_root_dir}/export/{project.title}/icons.zip', f"{media_root_dir}/export/{project.title}/icons/")
    delete_zip(f'{media_root_dir}/export/{project.title}/icons.zip')
    # shutil.copy(icons_path, f"{media_root_dir}/export/{project.title}/icons") 

    move_accessibility_icons(f"{media_root_dir}/uploads/icons", f"{media_root_dir}/export/{project.title}/icons/")

    # get uploaded images: thumbnails:create a zip
    thumbnail_path = f"{media_root_dir}/uploads/thumbnails/{project.title}"
    zip_directory(thumbnail_path, f'{media_root_dir}/export/{project.title}/thumbnails.zip')
    unzip_to_dir(f'{media_root_dir}/export/{project.title}/thumbnails.zip', f"{media_root_dir}/export/{project.title}/thumbnails/")
    delete_zip(f'{media_root_dir}/export/{project.title}/thumbnails.zip')

    # get the static files: css, js, fonts
    zip_directory(static_files_root_dir, f'{media_root_dir}/export/{project.title}/static.zip')
    unzip_to_dir(f'{media_root_dir}/export/{project.title}/static.zip', f"{media_root_dir}/export/{project.title}/")
    delete_zip(f'{media_root_dir}/export/{project.title}/static.zip')

    # get tiles'project/export/<title>/
    # get html file
    file_response = requests.get(f"{request.scheme }://{request.META['HTTP_HOST']}/project/export/{project.title}?lang=ar")
    with open(f'{path}/index_ar.html', 'w+', encoding='utf-8') as f:
        f.write(file_response.text)
    
    file_response = requests.get(f"{request.scheme }://{request.META['HTTP_HOST']}/project/export/{project.title}?lang=he")
    with open(f'{path}/index_he.html', 'w+', encoding='utf-8') as f:
        f.write(file_response.text)


    file_response = requests.get(f"{request.scheme }://{request.META['HTTP_HOST']}/project/export/{project.title}?lang=en")
    with open(f'{path}/index_en.html', 'w+', encoding='utf-8') as f:
        f.write(file_response.text)
    # zip the project folder and download the file
    zip_directory(f'{media_root_dir}/export/{project.title}', f'{media_root_dir}/export/{project.title}.zip')


    response = HttpResponse(open(f'{media_root_dir}/export/{project.title}.zip', 'rb').read())
    response['Content-Type'] = 'application/x-zip-compressed'
    response['Content-Disposition'] = f'attachment; filename={project.title}.zip'


    return response
    # return JsonResponse({"data":"Success"})

# user
def logout_view(request):
    logout(request)
    
    return redirect("/")