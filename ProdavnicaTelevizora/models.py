from django.db import models
from django.urls import reverse


# Create your models here.

class Dijagonala(models.Model):
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('naziv',)
        verbose_name = 'dijagonala'
        verbose_name_plural = 'dijagonale'

    def __str__(self): return self.naziv

    def ApsolutniURL(self):
        return reverse('ProdavnicaTelevizora:ListaTelevizoraPoDijagonaliEkrana', args=[self.slug])


class Televizor(models.Model):
    dijagonala = models.ForeignKey(Dijagonala, related_name='televizori', on_delete=models.CASCADE)
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    slika = models.ImageField(upload_to='televizori/%Y/%m/%d', blank=True)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    raspoloziv = models.BooleanField(default=True)
    kreiran = models.DateTimeField(auto_now_add=True)
    azuriran = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('naziv',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'televizori'

    def __str__(self): return self.naziv

    def ApsolutniURL(self):
        return reverse('ProdavnicaTelevizora:DetaljiTelevizora', args=[self.id, self.slug])
