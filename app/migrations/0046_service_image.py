# Generated by Django 5.0.2 on 2024-03-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default=1, upload_to='media/service/'),
            preserve_default=False,
        ),
    ]
