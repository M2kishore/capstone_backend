# Generated by Django 3.2.12 on 2022-04-05 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('typeform', '0007_rename_answer_answer_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='submitted_by',
        ),
    ]
