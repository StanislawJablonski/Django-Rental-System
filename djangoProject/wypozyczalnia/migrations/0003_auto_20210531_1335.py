# Generated by Django 3.1.7 on 2021-05-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia', '0002_auto_20210531_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocja',
            name='proc_rabatu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='promocja',
            name='data_rozpoczecia',
            field=models.DateTimeField(),
        ),
    ]
