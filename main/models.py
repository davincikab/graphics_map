from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TILES_OPTIONS = (
    (),
    ()
)

default_user = User.objects.get(id=1)

class CustomMaps(models.Model):
    title = models.CharField(max_length=200,null=False)
    description = models.TextField()
    tiles_folder = models.CharField(default="/media/uploads/projects/efteling", max_length=400)
    center = models.CharField(max_length=200, default="0,0", null=False)
    tiles_in_folders = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="./uploads/thumbnails")
    bearing = models.IntegerField(default=0, null=False)
    minzoom = models.IntegerField(default=0)
    maxzoom = models.IntegerField(default=5)

    class Meta:
        verbose_name_plural = "Custom Maps"

    def __str__(self):
        return self.title

READING_MODES = (
    ("RTL", "Right To Left"),
    ("LTR", "Left To Right")
)

class Project(models.Model):
    title = models.CharField(max_length=200,null=False)
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=default_user.pk)
    custom_map = models.ForeignKey(CustomMaps, on_delete=models.SET_NULL, null=True)
    reading_mode = models.CharField(choices=READING_MODES, default="RTL", max_length=50)

    class Meta:
        verbose_name_plural = "Projects"
    
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

    class Meta:
        verbose_name_plural = "Icons"

    def __str__(self):
        return self.title

class PinCategory(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    title = models.CharField(default="", max_length=200)
    icon = models.FileField(upload_to="./uploads/icons/")
    active_icon = models.FileField(upload_to="./uploads/icons/", default="uploads/icons/axe_active.png")

    class Meta:
        verbose_name_plural = "Pin Categories"

    def __str__(self):
        return self.title

class PinSubCategory(models.Model):
    category = models.ForeignKey(PinCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(default="", max_length=200)

    class Meta:
        verbose_name_plural = "Pin Sub Categories"    

    def __str__(self):
        return self.title

PIN_TYPES = (
    ("Area Pin", "Area Pin"),
    ("Detail Pin", "Detail Pin")
)

class Pins(models.Model):
    title = models.CharField(max_length=200,null=False)
    subtitle =models.CharField(max_length=200)
    pin_type = models.CharField(max_length=100, choices=PIN_TYPES, default="Detail Pin")
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    description = models.TextField(null=True)
    category = models.CharField(null=False, max_length=100, default="Attraction")
    subcategory = models.CharField(null=True, max_length=100)
    icon = models.CharField(null=False, max_length=1000)
    active_icon = models.CharField(null=False, max_length=1000, default="uploads/icons/axe_active.png")
    maxzoom = models.IntegerField(default=18)
    minzoom = models.IntegerField(default=0)
    bottom_link = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    location_image = models.ImageField(default="default.png", upload_to="./uploads/thumbnails/pin_images/")
    accesibility_features = models.JSONField(null=True)

    class Meta:
        verbose_name_plural = "Pins"

    def __str__(self):
        return self.title
