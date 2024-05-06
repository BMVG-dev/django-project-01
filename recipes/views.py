from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, './recipes/home.html', context={
        'name': 'BrunoPy dev'
    })


def contact(request):
    return render(request, './recipes/contact.html')


def about(request):
    return render(request, './recipes/about.html')
