# Generated by Django 3.0.6 on 2021-08-10 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mail.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
