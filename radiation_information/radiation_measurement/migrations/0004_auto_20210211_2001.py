# Generated by Django 3.1.6 on 2021-02-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiation_measurement', '0003_auto_20210211_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiation_measurement',
            name='type',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
