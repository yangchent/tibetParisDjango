# Generated by Django 3.1.14 on 2022-02-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220201_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='boutique',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='ngo',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='ngo',
            name='type',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='deliveroo',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='fork',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='link',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='uber',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
