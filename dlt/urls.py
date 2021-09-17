from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, {'pagename': ''}, name='home'),
    path('contact', views.contact, name='contact'),
    path('django_project', views.django_project, name='django_project'),
    path('<str:pagename>', views.index, name='index'),
]