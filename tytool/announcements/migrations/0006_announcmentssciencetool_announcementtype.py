# Generated by Django 3.1 on 2020-08-28 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0005_auto_20200828_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcmentssciencetool',
            name='announcementType',
            field=models.CharField(default=False, max_length=20),
        ),
    ]