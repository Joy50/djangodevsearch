# Generated by Django 5.0.6 on 2024-06-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='feature_image',
            field=models.ImageField(blank=True, default='favicon', null=True, upload_to=''),
        ),
    ]
