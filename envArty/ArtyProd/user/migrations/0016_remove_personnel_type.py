# Generated by Django 4.2 on 2023-05-06 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_remove_equipe_projet_personnel_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnel',
            name='type',
        ),
    ]