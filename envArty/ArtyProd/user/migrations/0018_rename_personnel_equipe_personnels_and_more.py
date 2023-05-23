# Generated by Django 4.2 on 2023-05-06 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_rename_personnels_equipe_personnel_equipe_projet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipe',
            old_name='personnel',
            new_name='personnels',
        ),
        migrations.RemoveField(
            model_name='equipe',
            name='projet',
        ),
        migrations.AddField(
            model_name='projet',
            name='equipe',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.equipe'),
        ),
    ]