# Generated by Django 3.0.6 on 2020-07-05 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0051_auto_20200705_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privateschools',
            name='opera_about',
        ),
        migrations.RemoveField(
            model_name='publicschools',
            name='opera_about',
        ),
        migrations.AlterField(
            model_name='region',
            name='hospitals',
            field=models.ManyToManyField(blank=True, to='boss.Hospital'),
        ),
    ]
