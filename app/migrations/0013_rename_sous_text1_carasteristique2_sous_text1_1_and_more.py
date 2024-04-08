# Generated by Django 5.0.2 on 2024-03-24 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_carasteristique2_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carasteristique2',
            old_name='sous_text1',
            new_name='sous_text1_1',
        ),
        migrations.RenameField(
            model_name='carasteristique2',
            old_name='sous_text2',
            new_name='sous_text1_2',
        ),
        migrations.RenameField(
            model_name='carasteristique2',
            old_name='sous_text3',
            new_name='sous_text1_3',
        ),
        migrations.RenameField(
            model_name='carasteristique2',
            old_name='sout_text',
            new_name='sous_text2_1',
        ),
        migrations.RenameField(
            model_name='carasteristique2',
            old_name='name',
            new_name='sous_titre1_1',
        ),
        migrations.RenameField(
            model_name='carasteristique2',
            old_name='sous_titre1',
            new_name='sous_titre1_2',
        ),
        migrations.RenameField(
            model_name='carasteristique2',
            old_name='sous_titre2',
            new_name='sous_titre1_3',
        ),
        migrations.RenameField(
            model_name='carasteristique2',
            old_name='sous_titre3',
            new_name='sous_titre2_1',
        ),
        migrations.RenameField(
            model_name='carasteristique2',
            old_name='title',
            new_name='sous_titre2_2',
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sous_text2_2',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sous_text2_3',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sous_text3_1',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sous_text3_2',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sous_text3_3',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sous_titre2_3',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sous_titre3_1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sous_titre3_2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sous_titre3_3',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sout_text1',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sout_text2',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='sout_text3',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='title1',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='title2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carasteristique2',
            name='title3',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
