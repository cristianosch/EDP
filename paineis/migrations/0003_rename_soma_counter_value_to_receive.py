# Generated by Django 4.0.3 on 2022-04-06 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paineis', '0002_remove_counter_value_remove_counter_value_per_panel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counter',
            old_name='soma',
            new_name='value_to_receive',
        ),
    ]
