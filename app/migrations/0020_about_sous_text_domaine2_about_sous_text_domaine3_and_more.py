# Generated by Django 5.0.2 on 2024-03-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='sous_text_domaine2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='sous_text_domaine3',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='sous_text_domaine4',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
