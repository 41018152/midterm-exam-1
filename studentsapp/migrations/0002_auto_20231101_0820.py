# Generated by Django 3.1.7 on 2023-11-01 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
