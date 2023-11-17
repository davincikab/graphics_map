#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class CustomMaps(models.Model):
    title = models.CharField(max_length=200,null=False)
    description = models.TextField()
    tiles_folder = models.FilePathField(default="/media/uploads/projects/efteling")
    center = models.CharField(max_length=200,null=False)
    thumbnail = models.ImageField(upload_to="../media/uploads/thumbnails")

    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=200,null=False)
    custom_map = models.ForeignKey(CustomMaps, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title

class Icons(models.Model):
    title = models.CharField(max_length=200,null=False)
    icon = models.FileField(upload_to="./media/uploads/icons/")

class Pins(models.Model):
    title = models.CharField(max_length=200,null=False)
    subtitle =models.CharField(max_length=200)
    #point_type=models.
    latitue = models.FloatField(default=0   )
    longitude = models.FloatField(default=0 )
    body = models.TextField()
    icon = models.ForeignKey(Icons, on_delete=models.SET_NULL, null=True)
    minzoom= models.IntegerField(default=0)
    maxzoom=models.IntegerField(default=18)
    bottom_link = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    
    