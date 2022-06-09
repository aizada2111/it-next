# Generated by Django 4.0.4 on 2022-06-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='images/%Y/%m/%d')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='images/%Y/%m/%d')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255)),
                ('number', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='images/%Y/%m/%d')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255)),
                ('mark', models.SmallIntegerField(default=0)),
                ('old_price', models.FloatField(blank=True)),
                ('new_price', models.FloatField(blank=True)),
                ('created', models.TimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='images/%Y/%m/%d')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='images/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('title', models.CharField(blank=True, db_index=True, max_length=255)),
            ],
        ),
    ]