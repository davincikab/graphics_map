from django.forms import ModelForm
from .models import Project, CustomMaps, Pins, Icons, PinCategory, PinSubCategory


class CustomMapsForm(ModelForm):
    class Meta:
        model = CustomMaps
        fields = ['title', 'description', 'bearing', 'minzoom', 'maxzoom', 'thumbnail', 'tiles_in_folders']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'custom_map', 'project_owner', 'project_language']

class IconsForm(ModelForm):
    class Meta:
        model = Icons
        fields = ['title', 'icon', 'icon_type']

class PinsForm(ModelForm):
    class Meta:
        model = Pins
        fields = ['title', 'subtitle', 'description', 'location_image', 'pin_type', 'more_info_link']
        # fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(PinsForm, self).__init__(*args, **kwargs)
        self.fields['more_info_link'].required = False

class PinCategoryForm(ModelForm):
    class Meta:
        model = PinCategory
        fields = ['title', 'project', 'is_area_category', 'icon', 'active_icon']

class PinSubCategoryForm(ModelForm):
    class Meta:
        model = PinSubCategory
        fields = ['category', 'title']
