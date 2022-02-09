# Generated by Django 3.0.5 on 2020-04-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200425_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=30, verbose_name='网站名字')),
            ],
            options={
                'verbose_name': '网站设置',
                'verbose_name_plural': '网站设置',
            },
        ),
    ]
