# Generated by Django 4.1.3 on 2022-11-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_project_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]