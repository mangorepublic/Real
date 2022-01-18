# Generated by Django 3.0.6 on 2020-07-04 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0047_auto_20200704_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='rev_about',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='insurance',
            name='rev_about',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='manufacturing',
            name='rev_about',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='hospitals',
            field=models.ManyToManyField(blank=True, to='boss.Hospital'),
        ),
    ]
