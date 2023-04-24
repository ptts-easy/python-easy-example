from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def IndexGetHandler(request):

  return redirect('/hello')

def HelloGetHandler(request):

  return HttpResponse("Hello")

def TemplateGetHandler(request):

  template = loader.get_template('index.html')

  ct = datetime.datetime.now()

  timestamp = int(ct.timestamp())

  context = {
    'title': 'Template',
    'template': 'template',
    'content': 'Hello World ...',
    'object': {'user': 'user001', 'msg':'msg001'},
    'timestamp': ['Apple', 'Banana', 'Cherry'],
    'timestamp_odd': timestamp % 2 == 1,
    'users': ['user1', 'user2', 'user3']
  }

  return HttpResponse(template.render(context, request))

def RouteDefaultGetHandler():

  template = loader.get_template('route.html')

  context = {
    'title': 'Route',
    'route': 'active',
    'act1': 'active',
    'message': 'This is default route',
    'content' : ''
  }

  return HttpResponse(template.render(context, request))
