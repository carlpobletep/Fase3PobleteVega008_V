# Generated by Django 3.1.3 on 2020-11-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cerveza',
            name='precio',
            field=models.IntegerField(null=True),
        ),
    ]
