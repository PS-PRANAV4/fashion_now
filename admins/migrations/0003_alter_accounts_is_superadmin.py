# Generated by Django 4.0.4 on 2022-05-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_accounts_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='is_superadmin',
            field=models.BooleanField(default=False),
        ),
    ]
