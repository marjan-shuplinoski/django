# Generated by Django 4.1.6 on 2023-02-24 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='pozajmeno_kniga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.books'),
        ),
    ]
