# Generated by Django 3.0.6 on 2020-07-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0043_auto_20200703_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='branches',
            field=models.ManyToManyField(blank=True, to='boss.branch'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='branches',
            field=models.ManyToManyField(blank=True, to='boss.branch'),
        ),
        migrations.AlterField(
            model_name='manufacturing',
            name='branches',
            field=models.ManyToManyField(blank=True, to='boss.branch'),
        ),
        migrations.AlterField(
            model_name='mining',
            name='branches',
            field=models.ManyToManyField(blank=True, to='boss.branch'),
        ),
    ]