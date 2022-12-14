# Generated by Django 4.1.1 on 2022-10-04 22:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizparticipant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_quizzes',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
