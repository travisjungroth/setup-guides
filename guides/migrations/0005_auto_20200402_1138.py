# Generated by Django 3.0.5 on 2020-04-02 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0004_auto_20200402_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verifications', to='guides.Step'),
        ),
    ]
