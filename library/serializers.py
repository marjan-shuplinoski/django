from .models import Members, Books
from rest_framework.serializers import ModelSerializer


class BooksSerializer(ModelSerializer):

    class Meta:
        model = Books
        fields = ['avtor','naslov','zanr','izdanie','jazik','maticna_kukja','kolicina','dostapni_izdanija']
    def create(self, validated_data):
        return super().create(validated_data)

class MembersSerializer(ModelSerializer):
    pozajmeno_kniga = BooksSerializer()

    class Meta:
        model = Members
        fields = ['ime_prezime', 'datum_zaclenuvanje', 'plateno', 'godini', 'adresa', 'grad', 'maticen_broj',
                  'email',
                  'tel_broj', 'zemeno', 'pozajmeno_kniga']

    def create(self, validated_data):
        return super().create(validated_data)
