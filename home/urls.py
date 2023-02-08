from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    path('portfolio/<str:title>', views.project, name='project'),
    path('blogs', views.blogs, name='blogs'),
    path('blog/<str:title>', views.blog, name='blog'),
    path('services/<str:service>', views.services, name='services'),
]