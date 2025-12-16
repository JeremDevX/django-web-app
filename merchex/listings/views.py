from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',
                  {'bands': bands})

def about(request):
    return HttpResponse('<h1> A propos </h1> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1> Contactez-nous </h1> <p>Envoyez-nous un email à contact@merchex.com</p>')

def listings(request):
    return HttpResponse('<h1> Listings de produits </h1> <p>Voici la liste de nos produits disponibles.</p>')