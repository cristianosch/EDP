# Generated by Django 4.0.3 on 2022-04-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paineis', '0013_remove_counter_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='total',
            field=models.FloatField(blank=True, default='0', null=True),
        ),
    ]