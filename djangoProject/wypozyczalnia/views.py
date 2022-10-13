from django.shortcuts import redirect

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import DetailView

from .forms import *
from .models import *

class WypozyczeniaView(TemplateView):
    template_name = 'wypozyczenia.html'

    def get_context_data(self, **kwargs):
        ctx = super(WypozyczeniaView, self).get_context_data(**kwargs)

        wypozyczenia = Wypozyczenie.objects.all()
        ctx['wypozyczenia'] = wypozyczenia

        return ctx

def wypozyczenie_edit(request, id):
    instance = get_object_or_404(Wypozyczenie, id=id)
    form = WypozyczenieForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/wypozyczalnia/wypozyczenia')
    return render(request, 'edit_form.html', {'form': form})


def wypozyczenie_delete(request, id):
    try:
        wypozyczenia_select = Wypozyczenie.objects.get(id=id)
    except Wypozyczenie.DoesNotExist:
        return redirect('/wypozyczalnia/wypozyczenia')
    wypozyczenia_select.delete()
    return redirect('/wypozyczalnia/wypozyczenia')


class AdresyView(TemplateView):
    template_name = 'adresy.html'

    def get_context_data(self, **kwargs):
        ctx = super(AdresyView, self).get_context_data(**kwargs)

        adresy = Adres.objects.all()
        ctx['adresy'] = adresy

        return ctx

def adres_edit(request, id):
    instance = get_object_or_404(Adres, id=id)
    form = AdresForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/wypozyczalnia/adresy')
    return render(request, 'edit_form.html', {'form': form})


def adres_delete(request, id):
    try:
        address_select = Adres.objects.get(id=id)
    except Adres.DoesNotExist:
        return redirect('/wypozyczalnia/adresy')
    address_select.delete()
    return redirect('/wypozyczalnia/adresy')


class KlienciView(TemplateView):
    template_name = 'klienci.html'

    def get_context_data(self, **kwargs):
        ctx = super(KlienciView, self).get_context_data(**kwargs)
        klienci = Klient.objects.all()
        ctx['klienci'] = klienci

        return ctx



class PracownicyView(TemplateView):
    template_name = 'pracownicy.html'

    def get_context_data(self, **kwargs):
        ctx = super(PracownicyView, self).get_context_data(**kwargs)

        pracownicy = Pracownik.objects.all()
        ctx['pracownicy'] = pracownicy

        return ctx

class WypozyczalnieView(TemplateView):
    template_name = 'wypozyczalnie.html'

    def get_context_data(self, **kwargs):
        ctx = super(WypozyczalnieView, self).get_context_data(**kwargs)

        wypozyczalnie = Wypozyczalnia.objects.all()
        ctx['wypozyczalnie'] = wypozyczalnie

        return ctx

class SprzetyView(TemplateView):
    template_name = 'sprzety.html'

    def get_context_data(self, **kwargs):
        ctx = super(SprzetyView, self).get_context_data(**kwargs)

        sprzety = Sprzet.objects.all()
        ctx['sprzety'] = sprzety

        return ctx

def sprzet_edit(request, id):
    instance = get_object_or_404(Sprzet, id=id)
    form = SprzetForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/wypozyczalnia/sprzety')
    return render(request, 'edit_form.html', {'form': form})


def sprzet_delete(request, id):
    try:
        sprzet_select = Sprzet.objects.get(id=id)
    except Sprzet.DoesNotExist:
        return redirect('/wypozyczalnia/sprzety')
    sprzet_select.delete()
    return redirect('/wypozyczalnia/sprzety')


class NaprawyView(TemplateView):
    template_name = 'naprawy.html'

    def get_context_data(self, **kwargs):
        ctx = super(NaprawyView, self).get_context_data(**kwargs)

        naprawy = Naprawa.objects.all()
        ctx['naprawy'] = naprawy

        return ctx

def naprawa_edit(request, id):
    instance = get_object_or_404(Naprawa, id=id)
    form = NaprawaForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/wypozyczalnia/naprawy')
    return render(request, 'edit_form.html', {'form': form})


def naprawa_delete(request, id):
    try:
        naprawa_select = Naprawa.objects.get(id=id)
    except Naprawa.DoesNotExist:
        return redirect('/wypozyczalnia/naprawy')
    naprawa_select.delete()
    return redirect('/wypozyczalnia/naprawy')


class PromocjeView(TemplateView):
    template_name = 'promocje.html'

    def get_context_data(self, **kwargs):
        ctx = super(PromocjeView, self).get_context_data(**kwargs)

        promocje = Promocja.objects.all()
        ctx['promocje'] = promocje

        return ctx

def promocja_edit(request, id):
    instance = get_object_or_404(Naprawa, id=id)
    form = PromocjaForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/wypozyczalnia/promocje')
    return render(request, 'edit_form.html', {'form': form})


def promocja_delete(request, id):
    try:
        promocja_select = Promocja.objects.get(id=id)
    except Promocja.DoesNotExist:
        return redirect('/wypozyczalnia/promocje')
    promocja_select.delete()
    return redirect('/wypozyczalnia/promocje')


class NewAdresView(CreateView):
    model = Adres
    fields = [
        'kraj','miasto','ulica','nr_domu','kod_pocz'
    ]
    template_name = 'addadres.html'

    def form_valid(self, form):
        new_adres = form.save(commit=False)
        new_adres.save()

        return super(NewAdresView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


class NewKlientView(CreateView):
    model = Klient
    fields = [
        'adres','imie','nazwisko','nr_tel'
    ]
    template_name = 'addklient.html'

    def form_valid(self, form):
        new_klient = form.save(commit=False)
        new_klient.save()

        return super(NewKlientView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

class NewPracownikView(CreateView):
    model = Pracownik
    fields = [
        'adres','imie','nazwisko','nr_tel','zarobki'
    ]
    template_name = 'addpracownik.html'

    def form_valid(self, form):
        new_klient = form.save(commit=False)
        new_klient.save()

        return super(NewPracownikView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

class NewWypozyczalniaView(CreateView):
    model = Wypozyczalnia
    fields = [
        'adres','nazwa','nr_tel'
    ]
    template_name = 'addwypozyczalnia.html'

    def form_valid(self, form):
        new_klient = form.save(commit=False)
        new_klient.save()

        return super(NewWypozyczalniaView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

class NewSprzetView(CreateView):
    model = Sprzet
    fields = [
        'marka','nazwa','ilosc','cena','kategoria','wypozyczalnia'
    ]
    template_name = 'addsprzet.html'

    def form_valid(self, form):
        new_klient = form.save(commit=False)
        new_klient.save()

        return super(NewSprzetView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

class NewNaprawaView(CreateView):
    model = Naprawa
    fields = [
        'opis','data_zgloszenia','czy_naprawione','data_naprawy','sprzet'
    ]
    template_name = 'addnaprawa.html'

    def form_valid(self, form):
        new_klient = form.save(commit=False)
        new_klient.save()

        return super(NewNaprawaView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

class NewPromocjaView(CreateView):
    model = Promocja
    fields = [
        'proc_rabatu','data_rozpoczecia','data_zakonczenia','sprzet'
    ]
    template_name = 'addpromocja.html'

    def form_valid(self, form):
        new_klient = form.save(commit=False)
        new_klient.save()

        return super(NewPromocjaView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


class NewWypozyczenieView(CreateView):
    model = Wypozyczenie
    fields = [
        'data_wydania','data_zwrotu','klient','pracownik','sprzet'
    ]
    template_name = 'addwypozyczenie.html'

    def form_valid(self, form):
        new_klient = form.save(commit=False)
        new_klient.save()

        return super(NewWypozyczenieView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

def DodajView(request):
    return render(request,'dodaj.html',{})