# Generated by Django 2.0.4 on 2018-04-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180405_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='path_imagem')),
                ('search_text', models.CharField(max_length=150, verbose_name='search_text')),
                ('descriptor', models.TextField(blank=True, null=True, verbose_name='descriptor')),
            ],
            options={
                'verbose_name_plural': 'Buscar',
                'verbose_name': 'Pesquisa',
                'ordering': ['search_text'],
            },
        ),
        migrations.DeleteModel(
            name='Search',
        ),
    ]
