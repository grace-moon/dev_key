# Generated by Django 3.2.5 on 2022-07-14 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keysite', '0005_rename_cmd_description_cmd_cmd_discription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cmd',
            old_name='cmd_discription',
            new_name='cmd_description',
        ),
    ]