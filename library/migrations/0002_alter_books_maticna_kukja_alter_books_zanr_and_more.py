# Generated by Django 4.1.6 on 2023-02-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='maticna_kukja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='zanr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='datum_zaclenuvanje',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='tel_broj',
            field=models.CharField(max_length=255, null=True),
        ),
    ]