# Generated by Django 3.2.6 on 2021-08-18 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_field_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.SmallIntegerField(null=True),
        ),
    ]
