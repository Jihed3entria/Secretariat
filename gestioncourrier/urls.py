from . import views
from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.views import login, logout

urlpatterns = [
   # url(r'^$', logout, dict(template_name='gestioncourrier/index.html'), name='acc'),
   #  url(r'^connecter$', login, dict(template_name='gestioncourrier/connect.html'), name='login1'),
   # url(r'^deconnecter$', logout, dict(template_name=''), name='logout'),
   # url(r'^recu-detail$', views.FirstView.as_view(), name='second'),
   # url(r'^chercher$', views.search, name="chercher"),
   # url(r'^acc$', views.Acceuil.as_view(), name='acceuil'),
  #  url('^', include('django.contrib.auth.urls')),
  #  url(r'^consulter$', views.Consulter.as_view(), name='consulter'),
  #  url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
  #  url(r'envoyes-detail$', views.det, name='courrierdetail'),
   # url(r'^courrier/ajouter/$', views.CourrierCreate.as_view(), name='courrier-add'),
  #  url(r'^courrier/(?P<pk>[0-9]+)/supprimer/$', views.CourrierDelete.as_view(), name='delete'),
   # url(r'^courrier/(?P<pk>[0-9]+)/$', views.CourrierUpdate.as_view(), name='courrier-update'),
  #  url(r'^register/$', views.UserFormView.as_view(), name='register'),
  #  url(r'^reprographie/$', views.responsableView.as_view(), name='responsable')

]
if settings.DEBUG == True :
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='img')]

