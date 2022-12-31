# Generated by Django 4.1.3 on 2022-12-31 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("addresses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]
