# Generated by Django 3.0.6 on 2020-07-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0025_auto_20200702_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='economy_about',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]