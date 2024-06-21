from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render(request, context))
    return render(request, 'index.html', {'name' : "Ajay"})


def contact(request):
    return HttpResponse("Contact")

def about(request):
    return HttpResponse("About")