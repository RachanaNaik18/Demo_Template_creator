from django.shortcuts import render,HttpResponseRedirect
from .models import *

# Create your views here.
def template_path(request):
    print(request.get_host())
    website_setting=Settings.objects.get(domain_name__name=request.get_host().split(":")[0])
    images=Images.objects.filter(website=website_setting.website)
    configs=Configuration.objects.filter(website=website_setting.website)

    
    context={
        "website":website_setting.website,
        "settings":website_setting,
        "images":images,
        "configs":configs
    }

    website_setting=Settings.objects.get(domain_name__name=request.get_host().split(":")[0])
    website_logo = Sections.objects.all().values_list("path", flat=True)
    print(website_logo)
    return render(request, "index.html",context)



