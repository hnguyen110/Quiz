# Generated by Django 4.1.2 on 2022-10-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('quiz_app', '0014_course_price_quiz_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
