# Generated by Django 2.2.10 on 2020-03-03 17:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='abcd1234', max_length=16),
        ),
    ]
