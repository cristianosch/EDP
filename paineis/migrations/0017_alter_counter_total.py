# Generated by Django 4.0.3 on 2022-04-26 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paineis', '0016_alter_counter_quantities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='total',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]