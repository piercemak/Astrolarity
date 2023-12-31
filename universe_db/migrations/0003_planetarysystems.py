# Generated by Django 4.2.2 on 2023-07-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("universe_db", "0002_auto_20230707_0117"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlanetarySystems",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("hostname", models.CharField(max_length=100)),
                ("number_of_stars", models.IntegerField()),
                ("number_of_planets", models.IntegerField()),
                ("discovery_method", models.CharField(max_length=100)),
                ("discovery_year", models.IntegerField()),
                ("discovery_facility", models.CharField(max_length=100)),
                ("orbit_period", models.FloatField(null=True)),
                ("radius", models.FloatField(null=True)),
                ("mass", models.FloatField(null=True)),
                ("equilibrium_temperature", models.FloatField(null=True)),
                ("spectral_type", models.CharField(max_length=50)),
                ("stellar_effective_temp", models.FloatField(null=True)),
                ("stellar_mass", models.FloatField(null=True)),
                ("stellar_metallicity", models.FloatField(null=True)),
                ("stellar_metallicity_ratio", models.CharField(max_length=50)),
                ("stellar_surface_gravity", models.FloatField(null=True)),
                ("ra", models.FloatField(null=True)),
                ("dec", models.FloatField(null=True)),
                ("distance", models.FloatField(null=True)),
                ("eccentricity", models.FloatField(null=True)),
            ],
        ),
    ]
