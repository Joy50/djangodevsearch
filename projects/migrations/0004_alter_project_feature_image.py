# Generated by Django 5.0.6 on 2024-06-06 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_feature_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='feature_image',
            field=models.ImageField(blank=True, default='icon.svg', null=True, upload_to=''),
        ),
    ]
