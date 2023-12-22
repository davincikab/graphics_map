# Generated by Django 4.2.7 on 2023-12-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_project_project_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='custommaps',
            name='map_style_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_theme',
            field=models.TextField(default='\n    --project-font:Poppins, sans-serif !important;\n    --project-font-he:Poppins, sans-serif !important;\n    --project-font-ar:Poppins, sans-serif !important;\n\n    --canvas-bg-color:#000000;\n    --area-text-color:#ffffff;\n    --filter-bg-color:#5F6F52;\n    --icons-bg:#A9B388;\n    --infobox-bg:#FEFAE0;\n    --text-color:#B99470;\n    --filter-card-active:#5F6F52;\n', max_length=1000),
        ),
    ]
