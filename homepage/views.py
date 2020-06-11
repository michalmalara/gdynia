from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import CreateNewUserForm, ChangePasswordForm

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


@login_required(login_url='zaloguj/')
def like_attraction(request):
    user = request.user

    attraction = Attraction.objects.get(id=request.GET['id'])
    if attraction.users_liked.filter(pk=user.pk).exists():
        attraction.users_liked.remove(user)
    else:
        attraction.users_liked.add(user)
    attraction.save()
    if 'return' in request.GET:
        return redirect(f'/atrakcja/{request.GET["id"]}')
    else:
        return redirect('/')


@login_required(login_url='zaloguj/')
def user_detail_view(request):
    user = User.objects.get(id=request.GET['id'])
    context = {'object': user}
    return render(request, 'registration/user_detail.html', context)


@login_required(login_url='zaloguj/')
def change_password(request):

    information = ''
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            if request.user.check_password(form.cleaned_data['old_password']):
                user = User.objects.get(id=request.user.id)
                user.set_password(form.cleaned_data['password1'])
                information = 'Hasło zostało zmienione'
            else:
                information = 'Wprowadź obecne hasło'
    else:
        form = ChangePasswordForm()

    context = {'form': form,
               'information': information}
    return render(request, 'registration/password_change_form.html', context)


class RegisterUserView(CreateView):
    model = User
    form_class = CreateNewUserForm
    # fields = ('email', 'username', 'password')
    template_name = 'registration/sign_in.html'
    success_url = '/'

