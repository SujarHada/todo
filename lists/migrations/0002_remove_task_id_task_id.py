# Generated by Django 4.2.1 on 2023-05-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AddField(
            model_name='task',
            name='ID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
