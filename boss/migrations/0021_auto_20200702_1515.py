# Generated by Django 3.0.6 on 2020-07-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0020_remove_region_covidhot_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='chri_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='muslim_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='other_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='tradi_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
