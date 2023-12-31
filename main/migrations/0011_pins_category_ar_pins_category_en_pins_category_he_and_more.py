# Generated by Django 4.2.7 on 2023-12-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_pinsubcategory_title_ar_pinsubcategory_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pins',
            name='category_ar',
            field=models.CharField(default='Attraction', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='category_en',
            field=models.CharField(default='Attraction', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='category_he',
            field=models.CharField(default='Attraction', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='description_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='description_he',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='subcategory_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='subcategory_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='subcategory_he',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='subtitle_ar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='subtitle_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='subtitle_he',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='title_ar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pins',
            name='title_he',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='title_ar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='title_he',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
