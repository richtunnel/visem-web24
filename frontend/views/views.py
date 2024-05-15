from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
     template_name = "frontend/pages/index.html"
     
     
class RicksPortfolio(TemplateView):
     template_name = "frontend/resume/index.html"