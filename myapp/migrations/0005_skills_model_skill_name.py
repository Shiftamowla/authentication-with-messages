# Generated by Django 5.1.1 on 2024-09-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_skills_model_skill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills_model',
            name='skill_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
