from django.shortcuts import render, get_object_or_404
from KorpaZaKupovinu.forms import FormaZaDodavanjeTelevizoraUKorpu
from .models import Dijagonala, Televizor
from KorpaZaKupovinu.korpa import Korpa


# Create your views here.
def ListaTelevizora(request, dijagonala_slug=None):  # vraca katalog kao html
    dijagonala = None
    dijagonale = Dijagonala.objects.all()
    televizori = Televizor.objects.filter(raspoloziv=True)
    if dijagonala_slug:
        dijagonala = get_object_or_404(Dijagonala, slug=dijagonala_slug)
        televizori = televizori.filter(dijagonala=dijagonala)
    korpa = Korpa(request)
    return render(request, 'ProdavnicaTelevizora/televizor/list.html',
                  {'dijagonala': dijagonala, 'dijagonale': dijagonale, 'televizori': televizori, 'korpa': korpa})


def DetaljiTelevizora(request, id, slug):
    televizor = get_object_or_404(Televizor, id=id, slug=slug, raspoloziv=True)
    korpa = Korpa(request)
    formazadodavanjeautomobilaukorpu = FormaZaDodavanjeTelevizoraUKorpu()
    return render(request, 'ProdavnicaTelevizora/televizor/detail.html',
                  {'televizor': televizor, 'formazadodavanjeautomobilaukorpu':
                      formazadodavanjeautomobilaukorpu,
                   'korpa': korpa})
