# Generated by Django 3.0.6 on 2020-07-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0023_auto_20200702_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='diversity_about',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
