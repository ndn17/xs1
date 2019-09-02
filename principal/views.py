from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='principal/base.html'
class MrRobotT1(TemplateView):
    template_name='principal/MrRobotT1.html'

class MrRobotT1001(TemplateView):
    template_name='principal/MrRobotT1001.html'


