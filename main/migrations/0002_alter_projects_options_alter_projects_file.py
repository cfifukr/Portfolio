# Generated by Django 4.2.4 on 2023-09-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterField(
            model_name='projects',
            name='file',
            field=models.FileField(upload_to='project-files/', verbose_name='Task File'),
        ),
    ]
