# Generated by Django 3.2.5 on 2022-07-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keysite', '0008_cmd_cmd_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmd',
            name='cmd_category',
            field=models.CharField(choices=[('Feaquently_Used_Key', 'Feaquently_Used_Key'), ('Ribbon', 'Ribbon'), ('Navigate', 'Navigate'), ('Preview', 'Preview'), ('Select', 'Select'), ('Extend_Selection', 'Extend_Selection'), ('Edit', 'Edit'), ('Align', 'Align'), ('Format', 'Format'), ('Insert', 'Insert'), ('Web', 'Web'), ('Table', 'Table'), ('Review', 'Review'), ('Reference', 'Reference'), ('Mail', 'Mail'), ('Field', 'Field'), ('Language', 'Language'), ('View', 'View'), ('Outline', 'Outline'), ('Fn_key', 'Fn_key')], max_length=200),
        ),
    ]
