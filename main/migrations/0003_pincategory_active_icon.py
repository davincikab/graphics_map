# Generated by Django 4.2.7 on 2023-12-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pins'),
    ]

    operations = [
        migrations.AddField(
            model_name='pincategory',
            name='active_icon',
            field=models.FileField(default='uploads/icons/axe_active.png', upload_to='./uploads/icons/'),
        ),
    ]
