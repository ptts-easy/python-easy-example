from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexGetHandler),
    path('hello', views.HelloGetHandler, name='HelloGetHandler'),
    path('template/', views.TemplateGetHandler, name='TemplateGetHandler'),
    path('route/', views.RouteDefaultGetHandler, name='RouteDefaultGetHandler'),    
]