# Generated by Django 2.2.1 on 2019-11-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191110_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='photo',
            field=models.ImageField(default='images/markets.png', upload_to='images/'),
        ),
    ]