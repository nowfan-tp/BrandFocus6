# Generated by Django 3.0.14 on 2023-04-03 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_delete_used_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usedcoupoon',
            old_name='Coupon',
            new_name='coupon',
        ),
    ]