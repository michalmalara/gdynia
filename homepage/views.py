from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from time import timezone

# import models
from .models import Attraction


# Create your views here.

class AttractionList(ListView):
    model = Attraction
    template_name = 'attractions.html'
    paginate_by = 10


class AttractionDetailView(DetailView):
    model = Attraction
    template_name = 'attraction_detail.html'

    def get_object(self):
        return get_object_or_404(Attraction, id=self.kwargs['id'])
