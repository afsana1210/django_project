# Generated by Django 3.1 on 2020-08-25 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECP', '0002_auto_20200824_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='user',
            field=models.CharField(choices=[('1', 'CONSUMER'), ('provider', 'PROVIDER')], default='provider', max_length=240),
        ),
    ]
