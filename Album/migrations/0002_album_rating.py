# Generated by Django 5.0.1 on 2024-02-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='Rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0, max_length=5),
        ),
    ]
