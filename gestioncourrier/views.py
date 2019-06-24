from django.utils.decorators import method_decorator
from .models import Courrier, CourrierR
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required




def search(request):
    template = 'gestioncourrier/consulter.html'
    query = request.GET.get('q')
    x = request.GET.get('radio')
    b = request.GET.get('radiobtn', None)
    results = Courrier.objects.all()

    if b == 'objet':
        results = Courrier.objects.filter(Q(objet__icontains=query))
    if b == 'destinataire':
        results = Courrier.objects.filter(Q(destinataire__icontains=query))
    if b == 'dateArrive':
        results = Courrier.objects.filter(Q(dateArrive__icontains=query))
    if b == 'expediteur':
        results = Courrier.objects.filter(Q(expediteur__icontains=query))

    context = {
        "object_list": results,
        "title": "List",
        "today": timezone.datetime.now(),
    }

    return render(request, template, context)
    # return render(request,template,)


class CourrierCreate(CreateView):
    model = Courrier
    fields = ['objet', 'expediteur', 'destinataire', 'piece_jointe', 'affichable', 'dateArrive', 'nom', 'surnom',
              'parcours']


class DetailView(generic.DetailView):
    model = Courrier
    template_name = 'gestioncourrier/consulter.html'


class Consulter(generic.ListView):
    template_name = 'gestioncourrier/consulter.html'

    # def search(request):
    #  query = request.GET.get('q')
    def get_queryset(self):
        return Courrier.objects.all()


class CourrierUpdate(UpdateView):
    model = Courrier
    fields = ['objet', 'expediteur', 'destinataire', 'piece_jointe', 'affichable', 'dateArrive', 'parcours', 'nom',
              'surnom']
    success_url = reverse_lazy('consulter')


class CourrierDelete(DeleteView):
    model = Courrier
    success_url = reverse_lazy('consulter')


class Acceuil(generic.ListView):
    template_name = 'gestioncourrier/acceuil.html'

    def get_queryset(self):
        return Courrier.objects.all()


class UserFormView(View):
    form_class = UserForm
    template_name = 'gestioncourrier/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # normalize date
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
        return render(request, self.template_name, {'form': form})
