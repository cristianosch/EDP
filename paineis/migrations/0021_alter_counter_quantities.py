# Generated by Django 4.0.3 on 2022-04-28 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paineis', '0020_alter_counter_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='quantities',
            field=models.FloatField(blank=True, default='0'),
        ),
    ]