# Generated by Django 4.1 on 2022-12-19 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labeling', '0009_alter_question_squestion_filter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='sQuestion_Filter',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tSkip',
        ),
    ]
