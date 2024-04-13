from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo',null=True, blank=True)
    about=models.TextField(null=True, blank=True)
    est_year=models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    image = models.ImageField(upload_to='employee',null=True, blank=True)
    address=models.CharField(max_length=255)

    def __str__(self):
        return self.role


class Sections(models.Model):
    position = models.CharField(max_length=30, unique=True)
    component_name=models.CharField(max_length=200)
    data_json=models.JSONField(null=True)
    path=models.TextField()

class Website(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    website_name=models.CharField(max_length=200)
    color_pallete=models.CharField(max_length=10)
    hover_color=models.CharField(max_length=10)
    sections = models.ManyToManyField(Sections)
    logo = models.ImageField(upload_to='logo',null=True, blank=True)

IMAGE_TYPE=(
    ("gallery","gallery"),
    ("amenities","amenities"),
    ("master plan","master plan"),
    ("floor plan","floor plan"),
    ("Cover Image","Cover Image"),
    ("Home","Home"),
    ("About us","About us"),
    
)

class Images(models.Model):
    img_type=models.CharField(max_length=200,default="gallery",choices=IMAGE_TYPE)
    item = models.ImageField(upload_to='gallery' ,null=True, blank=True)
    name=models.CharField(max_length=200)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)




CONFIG_CHOICES=(

    ("1 RK","1 RK"),
    ("1 BHK","1 BHK"),
    ("1.5 BHK","1.5 BHK"),
    ("2 BHK","1 2HK"),
    ("2.5 BHK","1 2.5HK"),
    ("3 BHK","1 BH3"),
    ("4 BHK","1 BH4"),
)

class Configuration(models.Model):
    config=models.CharField(max_length=200,choices=CONFIG_CHOICES)
    image = models.ImageField(upload_to='config',null=True, blank=True)
    measurements=models.JSONField(default=dict(
        carpet_area=0,
        rera_carpet_area=0,
        built_up_area=0,
        rera_built_up_area=0
    ))
    pricing=models.JSONField(default=dict(
        all_in=0,
        basic_price=0
    ))
    request_price=models.BooleanField(default=False)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)



class Domain(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Settings(models.Model):
    website=models.ForeignKey(Website, on_delete=models.CASCADE)
    domain_name=models.ManyToManyField(Domain)
    google_analytics = models.TextField(null=True, blank=True)
    meta_tag = models.TextField(null=True, blank=True)

