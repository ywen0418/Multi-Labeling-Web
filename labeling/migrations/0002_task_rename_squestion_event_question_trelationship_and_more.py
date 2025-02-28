# Generated by Django 4.1 on 2022-09-29 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labeling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdone', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='question',
            old_name='sQuestion_Event',
            new_name='tRelationship',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='sQuestion_Topic',
            new_name='tWork',
        ),
        migrations.DeleteModel(
            name='Summarization',
        ),
        migrations.AddField(
            model_name='task',
            name='tQuestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labeling.question'),
        ),
        migrations.AddField(
            model_name='task',
            name='tUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
