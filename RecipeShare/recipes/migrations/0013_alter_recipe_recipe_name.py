# Generated by Django 4.2.3 on 2023-08-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_remove_recipeingredient_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
