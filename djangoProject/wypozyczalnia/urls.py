from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import *


urlpatterns = [
    path('wypozyczenia/', views.WypozyczeniaView.as_view(), name='wypozyczenia'),
    path('wypozyczenia/wypozyczenie_edit/<int:id>', wypozyczenie_edit),
    path('wypozyczenia/wypozyczenie_delete/<int:id>', wypozyczenie_delete),


    path('adresy/', views.AdresyView.as_view(), name='adresy'),
    path('adresy/adres_edit/<int:id>', adres_edit),
    path('adresy/adres_delete/<int:id>', adres_delete),

    path('klienci/', views.KlienciView.as_view(), name='klienci'),

    path('pracownicy/', views.PracownicyView.as_view(), name='pracownicy'),

    path('wypozyczalnie/', views.WypozyczalnieView.as_view(), name='wypozyczalnie'),

    path('sprzety/', views.SprzetyView.as_view(), name='sprzety'),
    path('sprzety/sprzet_edit/<int:id>', sprzet_edit),
    path('sprzety/sprzet_delete/<int:id>', sprzet_delete),

    path('naprawy/', views.NaprawyView.as_view(), name='naprawy'),
    path('naprawy/naprawa_edit/<int:id>', naprawa_edit),
    path('naprawy/naprawa_delete/<int:id>', naprawa_delete),

    path('promocje/', views.PromocjeView.as_view(), name='promocje'),
    path('promocje/promocja_edit/<int:id>', promocja_edit),
    path('promocje/promocja_delete/<int:id>', promocja_delete),

    path('addadres/', views.NewAdresView.as_view(), name='addadres'),
    path('addklient/', views.NewKlientView.as_view(), name='addklient'),
    path('addpracownik/', views.NewPracownikView.as_view(), name='addpracownik'),
    path('addwypozyczalnia/', views.NewWypozyczalniaView.as_view(), name='addwypozyczalnia'),
    path('addsprzet/', views.NewSprzetView.as_view(), name='addsprzet'),
    path('addnaprawa/', views.NewNaprawaView.as_view(), name='addnaprawa'),
    path('addpromocja/', views.NewPromocjaView.as_view(), name='addpromocja'),
    path('addwypozyczenie/', views.NewWypozyczenieView.as_view(), name='addwypozyczenie'),
    path('dodaj/', views.DodajView)
]