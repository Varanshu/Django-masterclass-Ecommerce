# Generated by Django 3.1.6 on 2021-02-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
