# Generated by Django 3.0.7 on 2020-06-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200625_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmodel',
            name='new_url',
            field=models.CharField(default='xyz', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='urlmodel',
            name='old_url',
            field=models.CharField(max_length=500),
        ),
    ]
