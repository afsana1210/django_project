# Generated by Django 3.1 on 2020-08-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECP', '0003_auto_20200825_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='user',
            field=models.CharField(choices=[(2, 'CONSUMER'), (1, 'PROVIDER')], default='provider', max_length=240),
        ),
    ]
