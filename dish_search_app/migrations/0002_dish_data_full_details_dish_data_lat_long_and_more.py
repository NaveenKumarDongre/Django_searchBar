# Generated by Django 4.2.3 on 2023-07-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dish_search_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish_data",
            name="full_details",
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name="dish_data",
            name="lat_long",
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name="dish_data",
            name="items",
            field=models.TextField(default=None),
        ),
    ]