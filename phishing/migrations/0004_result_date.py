# Generated by Django 3.0.6 on 2021-06-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phishing', '0003_result_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
