# Generated by Django 4.2.7 on 2023-12-12 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomMaps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('tiles_folder', models.CharField(default='/media/uploads/projects/efteling', max_length=400)),
                ('center', models.CharField(default='0,0', max_length=200)),
                ('tiles_in_folders', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='./uploads/thumbnails')),
                ('minzoom', models.IntegerField(default=0)),
                ('maxzoom', models.IntegerField(default=5)),
            ],
            options={
                'verbose_name_plural': 'Custom Maps',
            },
        ),
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('icon_type', models.CharField(choices=[('Pin', 'Pin Icon'), ('Area', 'Area Icon'), ('Accesibility', 'Accessibility Icon')], default='Pin', max_length=100)),
                ('icon', models.FileField(upload_to='./uploads/icons/')),
            ],
            options={
                'verbose_name_plural': 'Icons',
            },
        ),
        migrations.CreateModel(
            name='PinCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('icon', models.FileField(upload_to='./uploads/icons/')),
            ],
            options={
                'verbose_name_plural': 'Pin Categories',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('reading_mode', models.CharField(choices=[('RTL', 'Right To Left'), ('LTR', 'Left To Right')], default='RTL', max_length=50)),
                ('custom_map', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.custommaps')),
                ('project_owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='PinSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.pincategory')),
            ],
            options={
                'verbose_name_plural': 'Pin Sub Categories',
            },
        ),
        migrations.AddField(
            model_name='pincategory',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.project'),
        ),
    ]
