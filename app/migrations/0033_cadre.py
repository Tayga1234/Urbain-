# Generated by Django 5.0.2 on 2024-03-26 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_methode1_methode2_methode3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/blog/')),
                ('name', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]