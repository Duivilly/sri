# Generated by Django 2.0.4 on 2018-04-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'ordering': ['textSearch'], 'verbose_name': 'Pesquisa', 'verbose_name_plural': 'Buscar'},
        ),
        migrations.AddField(
            model_name='search',
            name='descriptor',
            field=models.TextField(null=True, verbose_name='descriptor'),
        ),
        migrations.AlterField(
            model_name='search',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='path_imagem'),
        ),
    ]
