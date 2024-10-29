# Generated by Django 5.1.2 on 2024-10-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"verbose_name": "proyecto", "verbose_name_plural": "proyectos"},
        ),
        migrations.AddField(
            model_name="project",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="projects"),
        ),
    ]
