# Generated by Django 2.2.6 on 2019-11-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191119_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_tenant',
            field=models.BooleanField(default=False),
        ),
    ]