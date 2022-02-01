from django.urls import path
from . import views

app_name = 'prodavnicatelevizora'
urlpatterns = [path('', views.ListaTelevizora, name='ListaTelevizora'),
               path('<slug:dijagonala_slug>/', views.ListaTelevizora,
                    name='ListaTelevizoraPoDijagonaliEkrana'),
               path('<int:id>/<slug:slug>/', views.DetaljiTelevizora,
                    name='DetaljiTelevizora'), ]
