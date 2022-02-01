from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ProdavnicaTelevizora.models import Televizor
from .korpa import Korpa
from .forms import FormaZaDodavanjeTelevizoraUKorpu


# Create your views here.
@require_POST  # dekorator za prihvatanje POST zahteva
def DodajUKorpu(request, televizor_id):
    korpa = Korpa(request)
    televizor = get_object_or_404(Televizor, id=televizor_id)
    form = FormaZaDodavanjeTelevizoraUKorpu(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        korpa.Dodaj(televizor=televizor,
                    kolicina=cd['kolicina'],
                    dodati_na_kolicinu=cd['dodati_na_kolicinu'])
    return redirect('KorpaZaKupovinu:DetaljiKorpe')


@require_POST
def UkloniIzKorpe(request, televizor_id):
    korpa = Korpa(request)
    televizor = get_object_or_404(Televizor, id=televizor_id)
    korpa.Ukloni(televizor)
    return redirect('KorpaZaKupovinu:DetaljiKorpe')


def DetaljiKorpe(request):
    korpa = Korpa(request)
    for stavka in korpa:
        stavka['formazaazuriranjekolicine'] = FormaZaDodavanjeTelevizoraUKorpu(
            initial={'kolicina': 1, 'dodati_na_kolicinu': True})
    return render(request, 'KorpaZaKupovinu/detail.html', {'korpa': korpa})
