# Generated by Django 3.0.14 on 2023-04-03 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Used_Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Coupon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.Coupon')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
