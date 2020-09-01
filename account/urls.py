from . import views
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('index', views.index, name='index'),
    path('template', views.temp_demo, name='template-test'),
    path('signup', views.sign_up_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('', TemplateView.as_view(template_name='account/home.html'), name='home'),
    path('gallery/', TemplateView.as_view(template_name='account/gallery.html'), name='gallery'),
    path('about/', TemplateView.as_view(template_name='account/about.html'), name='about'),
]