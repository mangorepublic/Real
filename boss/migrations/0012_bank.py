# Generated by Django 3.0.6 on 2020-06-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0011_privateschools_publicschools'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(default='default.png', upload_to='')),
                ('population', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
