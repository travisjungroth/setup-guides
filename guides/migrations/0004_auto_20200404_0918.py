# Generated by Django 3.0.5 on 2020-04-04 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0003_auto_20200402_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]