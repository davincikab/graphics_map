# Generated by Django 4.2.7 on 2023-12-20 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_pins_more_info_link_ar_pins_more_info_link_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pins',
            name='bottom_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='reading_mode',
        ),
    ]
