# Generated by Django 5.0.2 on 2024-03-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_cadre'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadre',
            name='display',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
    ]
