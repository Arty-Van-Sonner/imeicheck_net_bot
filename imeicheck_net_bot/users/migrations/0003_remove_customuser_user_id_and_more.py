# Generated by Django 4.2.19 on 2025-02-10 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_id',
        ),
        migrations.AddField(
            model_name='customuser',
            name='telegram_user_id',
            field=models.IntegerField(db_column='telegram_user_id', null=True, unique=True),
        ),
    ]
