# Generated by Django 4.2.5 on 2023-09-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_answer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=''),
        ),
    ]
