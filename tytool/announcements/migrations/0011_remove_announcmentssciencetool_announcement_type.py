# Generated by Django 3.1 on 2020-08-28 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0010_auto_20200828_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcmentssciencetool',
            name='announcement_type',
        ),
    ]
