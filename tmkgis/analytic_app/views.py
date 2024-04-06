from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class AnalyticTemplateView(TemplateView):
    template_name = "analytic-page.html"