# Generated by Django 4.1.6 on 2023-02-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avtor', models.CharField(max_length=255)),
                ('naslov', models.CharField(max_length=255)),
                ('zanr', models.CharField(max_length=255)),
                ('izdanie', models.CharField(max_length=255)),
                ('jazik', models.CharField(max_length=255)),
                ('maticna_kukja', models.CharField(max_length=255)),
                ('kolicina', models.IntegerField()),
                ('dostapni_izdanija', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime_prezime', models.CharField(max_length=255)),
                ('datum_zaclenuvanje', models.DateTimeField()),
                ('plateno', models.BooleanField()),
                ('godini', models.IntegerField()),
                ('adresa', models.CharField(max_length=255)),
                ('grad', models.CharField(max_length=255)),
                ('maticen_broj', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('tel_broj', models.CharField(max_length=255)),
                ('zemeno', models.BooleanField()),
            ],
        ),
    ]