# Generated by Django 3.0.6 on 2020-07-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0002_auto_20200709_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='blackboard',
            field=models.TextField(),
        ),
    ]
