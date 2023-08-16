# Generated by Django 4.2.3 on 2023-08-09 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0047_lti1p3exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revealrule',
            name='trigger',
            field=models.IntegerField(choices=[(1, 'TRIGGER_MANUAL'), (2, 'TRIGGER_IMMEDIATE'), (3, 'TRIGGER_TIME'), (4, 'TRIGGER_DEADLINE'), (5, 'TRIGGER_DEADLINE_ALL'), (6, 'TRIGGER_COMPLETION'), (7, 'TRIGGER_DEADLINE_OR_FULL_POINTS')], verbose_name='LABEL_TRIGGER'),
        ),
    ]
