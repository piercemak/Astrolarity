# Generated by Django 4.2.2 on 2023-07-18 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("universe_db", "0005_alter_planetarysystems_stellar_metallicity_ratio"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="planetarysystems",
            options={
                "verbose_name": "Planetary System",
                "verbose_name_plural": "Planetary Systems",
            },
        ),
    ]
