from django.shortcuts import render
from . import models
# Home Page
def home(request):
	banners=models.Banners.objects.all()
	services=models.Service.objects.all()[:3]
	return render(request, 'home.html',{'banners':banners,'services':services})

