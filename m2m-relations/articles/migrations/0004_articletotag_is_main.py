# Generated by Django 3.2.9 on 2021-12-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211205_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletotag',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
