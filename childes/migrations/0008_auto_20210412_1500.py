# Generated by Django 3.0.6 on 2021-04-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childes', '0007_auto_20210412_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcript',
            name='child_gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('na', 'na')], default='MALE', max_length=6),
        ),
    ]
