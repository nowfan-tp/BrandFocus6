# Generated by Django 3.0.14 on 2023-04-06 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focusapp', '0005_auto_20230406_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shipping_address',
            new_name='shipping_add',
        ),
    ]
