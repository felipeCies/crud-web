# Generated by Django 5.1.7 on 2025-03-29 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estoque',
            old_name='data_vencimetno',
            new_name='data_vencimento',
        ),
    ]
