from django.contrib import admin
from .models import Members, Books, Vehicle, Person, Transakciska_smetka , Passport


# Register your models here.


class MembersAdmin(admin.ModelAdmin):
    list_display = ['ime_prezime', 'datum_zaclenuvanje', 'grad', 'godini', 'email', 'tel_broj', 'zemeno', 'plateno']
    list_filter = ['zemeno', 'plateno']


class BooksAdmin(admin.ModelAdmin):
    list_display = ['avtor', 'naslov', 'zanr', 'kolicina', 'dostapni_izdanija']
    list_filter = ['kolicina', 'dostapni_izdanija']


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['marka', 'model', 'godina', 'boja', 'max_brzina']
    list_filter = ['boja', 'max_brzina']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['ime', 'prezime', 'datum_na_ragjanje', 'embg', 'mesto_na_ziveenje', 'pol']
    list_filter = ['mesto_na_ziveenje', 'pol']


class TransSmetkaAdmin(admin.ModelAdmin):
    list_display = ['br_smetka', 'datum_na_otvaranje', 'sostojba', 'klient_id']

class PassportAdmin(admin.ModelAdmin):
    list_display = ['br_passport', 'datum_na_izdavanje', 'nacionalnost', 'person_id']


admin.site.register(Members, MembersAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Transakciska_smetka, TransSmetkaAdmin)
admin.site.register(Passport,PassportAdmin)
# Tipovi na relacija
# One 2 Many
# One 2 One
# Many 2 Many

# Django ORM  ( Object Relational Mapping )