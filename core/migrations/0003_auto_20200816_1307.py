# Generated by Django 3.1 on 2020-08-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200816_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescricao',
            name='data_presc',
            field=models.DateField(verbose_name='Data da Prescrição'),
        ),
    ]
