# Generated by Django 4.2.7 on 2023-12-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_pincategory_title_ar_pincategory_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pinsubcategory',
            name='title_ar',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pinsubcategory',
            name='title_en',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pinsubcategory',
            name='title_he',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]