# Generated by Django 4.0.3 on 2022-04-26 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paineis', '0010_delete_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counter',
            old_name='value_to_receive',
            new_name='values_to_receive',
        ),
    ]
