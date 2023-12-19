# Generated by Django 4.2.7 on 2023-12-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_project_lang_project_project_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_language',
            field=models.CharField(choices=[('en', 'English'), ('ar', 'Arabic'), ('he', 'Hebrew')], default='en', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='reading_mode',
            field=models.CharField(choices=[('RTL', 'Right To Left'), ('LTR', 'Left To Right')], default='en', max_length=50),
        ),
    ]
