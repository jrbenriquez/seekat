# Generated by Django 3.1.4 on 2021-01-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('se_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seeker',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
