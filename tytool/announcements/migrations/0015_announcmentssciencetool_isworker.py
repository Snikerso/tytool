# Generated by Django 3.1 on 2020-08-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0014_auto_20200828_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcmentssciencetool',
            name='isWorker',
            field=models.BooleanField(default=False),
        ),
    ]