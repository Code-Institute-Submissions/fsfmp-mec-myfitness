# Generated by Django 3.0.8 on 2020-08-18 08:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_auto_20200817_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='programs',
            name='post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
