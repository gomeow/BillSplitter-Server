from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^adduser/', views.adduser, name='adduser'),
    url(r'^removeuser/', views.removeuser, name='removeuser'),
    url(r'^info/', views.info, name='info'),
    url(r'^status/', views.status, name='status'),
]
