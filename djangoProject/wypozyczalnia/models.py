from django.db import models


class Adres(models.Model):
    kraj = models.CharField(max_length=50)
    miasto = models.CharField(max_length=50)
    ulica = models.CharField(max_length=50)
    nr_domu = models.CharField(max_length=10)
    kod_pocz = models.CharField(max_length=10)

    def __str__(self):
        return "{} {} {} {}".format(self.kraj, self.miasto,self.ulica,self.nr_domu)


class Klient(models.Model):
    adres = models.OneToOneField(Adres, on_delete=models.CASCADE, primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    nr_tel = models.CharField(max_length=20)

    def __str__(self):
        return "{} {} {} {}".format(self.imie, self.nazwisko, self.nr_tel, self.adres)


class Pracownik(models.Model):
    adres = models.OneToOneField(Adres, on_delete=models.CASCADE, primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    nr_tel = models.CharField(max_length=20)
    zarobki = models.IntegerField()

    def __str__(self):
        return "{} {} {} {}".format(self.imie, self.nazwisko, self.zarobki, self.adres)


class Wypozyczalnia(models.Model):
    adres = models.OneToOneField(Adres, on_delete=models.CASCADE, primary_key=True)
    nazwa = models.CharField(max_length=100)
    nr_tel = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.adres, self.nazwa)


class Sprzet(models.Model):
    marka = models.CharField(max_length=50)
    nazwa = models.CharField(max_length=50)
    ilosc = models.IntegerField()
    cena = models.FloatField(max_length=10)
    kategoria = models.CharField(max_length=50)
    wypozyczalnia = models.ForeignKey(Wypozyczalnia, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.marka, self.nazwa,self.kategoria)


class Naprawa(models.Model):
    opis = models.CharField(max_length=100)
    data_zgloszenia = models.DateTimeField()
    czy_naprawione = models.BooleanField()
    data_naprawy = models.DateTimeField()
    sprzet = models.ForeignKey(Sprzet, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.opis, self.sprzet)

class Promocja(models.Model):
    proc_rabatu = models.IntegerField(default=0)
    data_rozpoczecia = models.DateTimeField()
    data_zakonczenia = models.DateTimeField()
    sprzet = models.ForeignKey(Sprzet, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.sprzet, self.proc_rabatu)

class Wypozyczenie(models.Model):
    data_wydania = models.DateTimeField()
    data_zwrotu = models.DateTimeField()
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    sprzet = models.ForeignKey(Sprzet, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {}".format(self.klient, self.sprzet, self.data_wydania,self.data_zwrotu)