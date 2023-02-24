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

class Members(models.Model):
    ime_prezime = models.CharField(max_length=255)
    datum_zaclenuvanje = models.DateTimeField()
    plateno = models.BooleanField()
    godini = models.IntegerField()
    adresa = models.CharField(max_length=255)
    grad = models.CharField(max_length=255)
    maticen_broj = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tel_broj = models.CharField(max_length=255)
    zemeno = models.BooleanField()

class Books(models.Model):
    avtor = models.CharField(max_length=255)
    naslov = models.CharField(max_length=255)
    zanr = models.CharField(max_length=255)
    izdanie = models.CharField(max_length=255)
    jazik = models.CharField(max_length=255)
    maticna_kukja = models.CharField(max_length=255)
    kolicina = models.IntegerField()
    dostapni_izdanija = models.IntegerField()


