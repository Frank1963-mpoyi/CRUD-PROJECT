# Generated by Django 3.2 on 2021-05-16 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_employee_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.SlugField(blank=True, default='hello', unique=True),
        ),
    ]
