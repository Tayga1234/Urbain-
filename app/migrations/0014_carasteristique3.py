# Generated by Django 5.0.2 on 2024-03-24 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_sous_text1_carasteristique2_sous_text1_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carasteristique3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200)),
                ('titre', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=200)),
            ],
        ),
    ]
