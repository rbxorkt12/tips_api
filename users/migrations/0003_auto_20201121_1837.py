# Generated by Django 3.1.3 on 2020-11-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201009_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_kind',
            new_name='user_kind1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='point',
        ),
        migrations.AddField(
            model_name='profile',
            name='credit',
            field=models.IntegerField(default=800000),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_kind2',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
