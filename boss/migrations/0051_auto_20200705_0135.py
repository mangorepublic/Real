# Generated by Django 3.0.6 on 2020-07-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0050_auto_20200705_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondaryschools',
            name='acaperf_about',
        ),
        migrations.RemoveField(
            model_name='secondaryschools',
            name='admission_about',
        ),
        migrations.AlterField(
            model_name='region',
            name='hospitals',
            field=models.ManyToManyField(blank=True, to='boss.Hospital'),
        ),
    ]
