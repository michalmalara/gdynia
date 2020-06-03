from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# import models
from .models import Attraction


# Create your views here.

class AttractionList(ListView):
    model = Attraction
    template_name = 'attractions.html'
    paginate_by = 20
