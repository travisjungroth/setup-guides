# Generated by Django 3.0.5 on 2020-04-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0003_auto_20200402_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='requirements',
            field=models.ManyToManyField(blank=True, through='guides.Requirement', to='guides.Step'),
        ),
    ]
