# Generated by Django 4.2.3 on 2023-08-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_method',
            field=models.TextField(default=''),
        ),
    ]
