# Generated by Django 5.0.4 on 2024-04-12 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_sections_component_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='component_name',
            field=models.CharField(max_length=200),
        ),
    ]
