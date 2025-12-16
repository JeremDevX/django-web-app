from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""

        <h1>Hello Django !</h1>

        <p>Mes groupes préférés sont :<p>

        <ul>

            <li>{bands[0].name}</li>

            <li>{bands[1].name}</li>

            <li>{bands[2].name}</li>

        </ul>
        <p>Voici quelques listings de produits :</p>
        <ul>
            <li>{Listing.objects.all()[0].title}</li>
            <li>{Listing.objects.all()[1].title}</li>
            <li>{Listing.objects.all()[2].title}</li>
            <li>{Listing.objects.all()[3].title}</li>
        </ul>

""")

def about(request):
    return HttpResponse('<h1> A propos </h1> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1> Contactez-nous </h1> <p>Envoyez-nous un email à contact@merchex.com</p>')

def listings(request):
    return HttpResponse('<h1> Listings de produits </h1> <p>Voici la liste de nos produits disponibles.</p>')