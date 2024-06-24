from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render(request, context))
    return render(request, 'index.html', {'name' : "ashjgfdjhasfgdjh"})


def contact(request):
    # return HttpResponse("Contact")
    return render(request, 'contact.html')

def about(request):
    # return HttpResponse("About")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("Services")
    return render(request, 'services.html')