# Generated by Django 4.1.3 on 2024-02-25 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coordinatesapi', '0004_alter_weddingplanner_planner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couple',
            name='first_guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='couple_firsts', to='coordinatesapi.guest'),
        ),
        migrations.AlterField(
            model_name='couple',
            name='second_guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='couple_seconds', to='coordinatesapi.guest'),
        ),
    ]
