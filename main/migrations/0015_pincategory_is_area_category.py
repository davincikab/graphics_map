# Generated by Django 4.2.7 on 2023-12-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_pins_bottom_link_remove_project_reading_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='pincategory',
            name='is_area_category',
            field=models.BooleanField(default=False),
        ),
    ]
