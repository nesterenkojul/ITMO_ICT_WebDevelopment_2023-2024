# Generated by Django 4.2.7 on 2023-11-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_app", "0002_user_broker_user_manufacturer_user_role_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="size",
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
