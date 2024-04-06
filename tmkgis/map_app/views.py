from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MapsTemplateView(TemplateView):
    template_name = "map-page.html"