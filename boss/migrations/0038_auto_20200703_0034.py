# Generated by Django 3.0.6 on 2020-07-03 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0037_auto_20200703_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='privateschools',
            name='cost_about',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='publicschools',
            name='cost_about',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='privateschools',
            name='about',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
