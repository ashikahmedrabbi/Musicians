# Generated by Django 5.0.1 on 2024-02-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0002_alter_musician_first_name_alter_musician_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='Instrument_Type',
            field=models.CharField(choices=[('1', 'Guitar'), ('2', 'Piano'), ('3', 'Drums'), ('4', 'Violin'), ('5', 'Trumpet')], default=0, max_length=1),
        ),
    ]
