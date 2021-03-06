# Generated by Django 3.0.6 on 2021-06-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phishing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(max_length=200, null=True)),
                ('label', models.CharField(max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='CronData',
        ),
    ]
