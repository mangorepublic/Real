# Generated by Django 3.0.6 on 2020-07-02 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0033_region_shs_schools'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicschools',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='publicschools',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='publicschools',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='publicschools',
            name='tel',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='publicschools',
            name='about',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
