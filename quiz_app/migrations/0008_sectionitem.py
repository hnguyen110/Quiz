# Generated by Django 4.1.2 on 2022-10-13 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0007_coursesection'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content_type', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('order', models.IntegerField()),
                ('course_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='quiz_app.coursesection')),
            ],
        ),
    ]
