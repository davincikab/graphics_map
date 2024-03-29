# Generated by Django 4.2.7 on 2024-01-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_alter_project_project_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_theme',
            field=models.TextField(default='\n    --project-font:Poppins, sans-serif !important;\n    --project-font-he:Poppins, sans-serif !important;\n    --project-font-ar:Poppins, sans-serif !important;\n\n    --simple-text-offset:1;\n    --area-text-offset:3.2;\n    --simple-text-minzoom:14;\n    --simple-icon-minzoom:14;\n    --area-icon-minzoom:2;\n    --canvas-bg-color:#000000;\n    --area-text-color:#ffffff;\n    --simple-text-color:#000;\n    --filter-bg-color:#5F6F52;\n    --icons-bg:#A9B388;\n    --infobox-bg:#FEFAE0;\n    --text-color:#B99470;\n    --filter-card-active:#5F6F52;\n', max_length=1000),
        ),
    ]
