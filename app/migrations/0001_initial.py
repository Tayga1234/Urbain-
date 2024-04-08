# Generated by Django 5.0.2 on 2024-03-22 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='media/')),
                ('title', models.CharField(max_length=200)),
                ('onglet_1', models.CharField(max_length=200)),
                ('onglet_2', models.CharField(max_length=200)),
                ('onglet_3', models.CharField(max_length=200)),
                ('onglet_4', models.CharField(max_length=200)),
            ],
        ),
    ]