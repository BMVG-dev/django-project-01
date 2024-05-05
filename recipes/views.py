from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('HOME2')

def contact(request):
    return HttpResponse('CONTACT')

def about(request):
    return HttpResponse('ABOUT')