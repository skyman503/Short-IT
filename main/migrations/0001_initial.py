# Generated by Django 3.0.7 on 2020-06-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('og_url', models.URLField(max_length=500)),
                ('new_url', models.URLField(max_length=50, null=True)),
            ],
        ),
    ]
