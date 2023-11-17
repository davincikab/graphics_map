from django.forms import ModelForm
from .models import Project, CustomMaps, Pins, Icons


class CustomMapsForm(ModelForm):
    class Meta:
        model = CustomMaps
        fields = ['title', 'description', 'thumbnail']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'custom_map']

class IconsForm(ModelForm):
    class Meta:
        model = Icons
        fields = ['title', 'icon']

class PinsForm(ModelForm):
    class Meta:
        model = Pins
        fields = ['title', 'subtitle', 'body', 'minzoom', 'maxzoom']
        # fields = '__all__'

