# Generated by Django 3.0.6 on 2020-07-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0021_auto_20200702_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='diversity_about',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
