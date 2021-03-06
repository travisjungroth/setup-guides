# Generated by Django 3.0.5 on 2020-04-03 03:00

from django.db import migrations, models


def set_defaults(apps, schema_editor):
    Step = apps.get_model('guides', 'Step')
    for step in Step.objects.all():
        step.slug = '-'.join(step.title.lower().split())
        step.save()


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0001_initial_squashed_0005_auto_20200402_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='step',
            name='slug',
            field=models.SlugField(default=None, null=True),
        ),
        migrations.RunPython(set_defaults, reverse_func),
        migrations.AlterField(
            model_name='step',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='guide',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
