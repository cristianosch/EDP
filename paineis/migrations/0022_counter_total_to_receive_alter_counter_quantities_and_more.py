# Generated by Django 4.0.3 on 2022-04-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paineis', '0021_alter_counter_quantities'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='total_to_receive',
            field=models.FloatField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='counter',
            name='quantities',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='total',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
