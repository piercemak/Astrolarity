# Generated by Django 4.2.2 on 2023-07-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("universe_db", "0003_planetarysystems"),
    ]

    operations = [
        migrations.AlterField(
            model_name="planetarysystems",
            name="spectral_type",
            field=models.CharField(max_length=50, null=True),
        ),
    ]