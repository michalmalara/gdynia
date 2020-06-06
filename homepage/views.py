from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import CreateNewUserForm

# import models
from .models import Attraction
from user.models import User


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


# class UserDetailView(DetailView):
#     model = User
#     template_name = "user_detail.html"
#
#     def get_object(self):
#         return get_object_or_404(User, id=self.kwargs['id'])


class RegisterUserView(CreateView):
    model = User
    form_class = CreateNewUserForm
    # fields = ('email', 'username', 'password')
    template_name = 'registration/sign_in.html'
    success_url = '/'
