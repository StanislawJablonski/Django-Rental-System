from django import forms
from .models import *


class AdresForm(forms.ModelForm):
    class Meta:
        model = Adres
        fields = "__all__"

class KlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = "__all__"


class PracownikForm(forms.ModelForm):
    class Meta:
        model = Pracownik
        fields = "__all__"

class WypozyczalniaForm(forms.ModelForm):
    class Meta:
        model = Wypozyczalnia
        fields = "__all__"

class SprzetForm(forms.ModelForm):
    class Meta:
        model = Sprzet
        fields = "__all__"

class NaprawaForm(forms.ModelForm):
    class Meta:
        model = Naprawa
        fields = "__all__"

class PromocjaForm(forms.ModelForm):
    class Meta:
        model = Promocja
        fields = "__all__"

class WypozyczenieForm(forms.ModelForm):
    class Meta:
        model = Wypozyczenie
        fields = "__all__"