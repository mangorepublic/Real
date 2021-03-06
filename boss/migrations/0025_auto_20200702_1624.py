# Generated by Django 3.0.6 on 2020-07-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0024_auto_20200702_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondarySchools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
                ('cost', models.CharField(blank=True, max_length=200, null=True)),
                ('admission', models.CharField(blank=True, max_length=200, null=True)),
                ('about', models.CharField(blank=True, max_length=500, null=True)),
                ('enrolment', models.CharField(blank=True, max_length=200, null=True)),
                ('graduates', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='region',
            old_name='schools',
            new_name='private_schools',
        ),
        migrations.AddField(
            model_name='region',
            name='public_schools',
            field=models.ManyToManyField(to='boss.PublicSchools'),
        ),
        migrations.AddField(
            model_name='region',
            name='shs_schools',
            field=models.ManyToManyField(to='boss.SecondarySchools'),
        ),
    ]
