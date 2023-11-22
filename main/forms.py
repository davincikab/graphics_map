from django.forms import ModelForm
from .models import Project, CustomMaps, Pins, Icons


class CustomMapsForm(ModelForm):
    class Meta:
        model = CustomMaps
        fields = ['title', 'description', 'minzoom', 'maxzoom', 'thumbnail', 'tiles_in_folders']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'custom_map']

class IconsForm(ModelForm):
    class Meta:
        model = Icons
        fields = ['title', 'icon', 'icon_type']

class PinsForm(ModelForm):
    class Meta:
        model = Pins
        fields = ['title', 'subtitle', 'description', 'location_image', 'pin_type']
        # fields = '__all__'

