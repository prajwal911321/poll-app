# Generated by Django 4.2.1 on 2023-05-30 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Question',
            new_name='question',
        ),
    ]
