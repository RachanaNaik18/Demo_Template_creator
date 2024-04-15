# Generated by Django 5.0.4 on 2024-04-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_configuration_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='measurements',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='pricing',
        ),
        migrations.AddField(
            model_name='configuration',
            name='al_in',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='basic_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='rera_carpet_area',
            field=models.IntegerField(null=True),
        ),
    ]
