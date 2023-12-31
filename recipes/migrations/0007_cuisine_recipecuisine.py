# Generated by Django 4.2.3 on 2023-08-01 18:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipeingredient_recipe_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cuisine_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeCuisine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cuisine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.cuisine')),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
    ]
