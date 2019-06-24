from gestioncourrier.models import Courrier
from django.views import generic


class home(generic.ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return Courrier.objects.filter(affichable=True)
