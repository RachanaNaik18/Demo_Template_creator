# Generated by Django 5.0.4 on 2024-04-12 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_sections_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='Website',
            new_name='website',
        ),
    ]
