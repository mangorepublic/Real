# Generated by Django 3.0.6 on 2020-07-02 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0022_region_diversity_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='diversity_about',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
