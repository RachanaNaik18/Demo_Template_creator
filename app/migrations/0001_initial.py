# Generated by Django 5.0.4 on 2024-04-12 05:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo')),
                ('about', models.TextField(blank=True, null=True)),
                ('est_year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30, unique=True)),
                ('component_name', models.CharField(max_length=200)),
                ('data_json', models.JSONField(null=True)),
                ('path', models.FilePathField(path='easy_landing/app/templates/sections')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='employee')),
                ('address', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(max_length=200)),
                ('color_pallete', models.CharField(max_length=10)),
                ('hover_color', models.CharField(max_length=10)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
                ('sections', models.ManyToManyField(to='app.sections')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.URLField()),
                ('google_analytics', models.TextField(blank=True, null=True)),
                ('meta_tag', models.TextField(blank=True, null=True)),
                ('Website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.website')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_type', models.CharField(choices=[('gallery', 'gallery'), ('amenities', 'amenities'), ('master plan', 'master plan'), ('floor plan', 'floor plan'), ('Cover Image', 'Cover Image')], default='gallery', max_length=200)),
                ('item', models.ImageField(blank=True, null=True, upload_to='gallery')),
                ('name', models.CharField(max_length=200)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.website')),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.CharField(choices=[('1 RK', '1 RK'), ('1 BHK', '1 BHK'), ('1.5 BHK', '1.5 BHK'), ('2 BHK', '1 2HK'), ('2.5 BHK', '1 2.5HK'), ('3 BHK', '1 BH3'), ('4 BHK', '1 BH4')], max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='config')),
                ('measurements', models.JSONField(default={'built_up_area': 0, 'carpet_area': 0, 'rera_built_up_area': 0, 'rera_carpet_area': 0})),
                ('pricing', models.JSONField(default={'all_in': 0, 'basic_price': 0})),
                ('request_price', models.BooleanField(default=False)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.website')),
            ],
        ),
    ]
