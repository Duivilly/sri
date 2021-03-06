# Generated by Django 2.0.4 on 2018-05-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20180429_1526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseimage',
            options={'ordering': ['search_image'], 'verbose_name': 'SearchImagem', 'verbose_name_plural': 'BaseImage'},
        ),
        migrations.RemoveField(
            model_name='baseimage',
            name='descriptor',
        ),
        migrations.AddField(
            model_name='baseimage',
            name='descriptorBIC',
            field=models.TextField(blank=True, null=True, verbose_name='descriptorBIC'),
        ),
        migrations.AddField(
            model_name='baseimage',
            name='descriptorBIC_part',
            field=models.TextField(blank=True, null=True, verbose_name='descriptorBIC_part'),
        ),
        migrations.AddField(
            model_name='baseimage',
            name='descriptorCEDD',
            field=models.TextField(blank=True, null=True, verbose_name='descriptorCEDD'),
        ),
    ]
