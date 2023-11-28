#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
TILES_OPTIONS = (
    (),
    ()
)


class CustomMaps(models.Model):
    title = models.CharField(max_length=200,null=False)
    description = models.TextField()
    tiles_folder = models.CharField(default="/media/uploads/projects/efteling", max_length=400)
    center = models.CharField(max_length=200, default="0,0", null=False)
    tiles_in_folders = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="./uploads/thumbnails")
    minzoom = models.IntegerField(default=0)
    maxzoom = models.IntegerField(default=5)

    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=200,null=False)
    custom_map = models.ForeignKey(CustomMaps, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title

ICON_TYPES = (
    ("Pin", "Pin Icon"),
    ("Area", "Area Icon"),
    ("Accesibility", "Accessibility Icon")
)

class Icons(models.Model):
    title = models.CharField(max_length=200,null=False)
    icon_type = models.CharField(max_length=100, choices=ICON_TYPES, default="Pin")
    icon = models.FileField(upload_to="./uploads/icons/")

    def __str__(self):
        return self.title

PIN_TYPES = (
    ("Area Pin", "Area Pin"),
    ("Detail Pin", "Detail Pin")
)

class Pins(models.Model):
    title = models.CharField(max_length=200,null=False)
    subtitle =models.CharField(max_length=200)
    #point_type=models.
    pin_type = models.CharField(max_length=100, choices=PIN_TYPES, default="Detail Pin")
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    description = models.TextField(null=True)
    icon = models.CharField(default="icon.png", max_length=200)
    poi_category = models.CharField(default="", max_length=200) 
    maxzoom = models.IntegerField(default=18)
    minzoom = models.IntegerField(default=0)
    bottom_link = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    location_image = models.ImageField(default="default.png", upload_to="./uploads/thumbnails/pin_images/")
    accesibility_features = models.JSONField(null=True)

    def __str__(self):
        return self.title