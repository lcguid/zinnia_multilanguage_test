from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
  if request.LANGUAGE_CODE == 'pt-br':
    return HttpResponse("You prefer to read PT_BR.")
  elif request.LANGUAGE_CODE == 'en':
    return HttpResponse("You prefer to read EN.")
  else:
    return HttpResponse("You prefer to read another language.")
