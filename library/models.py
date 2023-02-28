from django.db import models


# Create your models here.
# Tabeli

# Clenovi
# (string, integer, float, boolean, date)
# Ime i prezime           string
# Zaclenvanje datum       date
# Dali plateno            boolean
# Adresa na ziveenje      string
# Grad                string
# Maticen broj            string
# Godini              int
# Email               string
# Telefonski broj     string
# Dali ima zemeno     boolean

# Knigi
# Ime i prezime na avtor      string
# Naslov na kniga     string
# Zanr na knigi           string
# Izdanie         string
# Jazik               string
# Maticna kukja           string
# Kolicina            int
# Dostapni izdanija       int




class Books(models.Model):
    avtor = models.CharField(max_length=255)
    naslov = models.CharField(max_length=255)
    zanr = models.CharField(max_length=255, null=True, blank=True)
    izdanie = models.CharField(max_length=255)
    jazik = models.CharField(max_length=255)
    maticna_kukja = models.CharField(max_length=255, null=True, blank=True)
    kolicina = models.IntegerField()
    dostapni_izdanija = models.IntegerField()

class Members(models.Model):
    ime_prezime = models.CharField(max_length=255)
    datum_zaclenuvanje = models.DateTimeField(auto_now_add=True)
    plateno = models.BooleanField()
    godini = models.IntegerField()
    adresa = models.CharField(max_length=255)
    grad = models.CharField(max_length=255)
    maticen_broj = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    tel_broj = models.CharField(max_length=255, null=True, blank=True)
    zemeno = models.BooleanField()
    pozajmeno_kniga = models.ForeignKey(Books, on_delete=models.CASCADE,null=True)

class Vehicle(models.Model):
    marka = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    godina = models.DateField(auto_now_add=True)
    br_na_sedista = models.IntegerField()
    boja = models.CharField(max_length=255)
    max_brzina = models.IntegerField()


class Person(models.Model):
    ime = models.CharField(max_length=255)
    prezime = models.CharField(max_length=255)
    datum_na_ragjanje = models.DateField()
    embg = models.IntegerField()
    mesto_na_ziveenje = models.CharField(max_length=255)
    pol = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Transakciska_smetka(models.Model):
    br_smetka = models.IntegerField()
    datum_na_otvaranje = models.DateField()
    sostojba = models.IntegerField()
    klient_id = models.ForeignKey(Person, on_delete=models.CASCADE,null=True)

class Passport(models.Model):
    br_passport = models.IntegerField()
    datum_na_izdavanje = models.DateField()
    izdaden_od = models.CharField(max_length=255)
    nacionalnost = models.CharField(max_length=255)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE,null=True)
