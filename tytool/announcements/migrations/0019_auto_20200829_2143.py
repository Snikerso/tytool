# Generated by Django 3.1 on 2020-08-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0018_auto_20200829_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcmentssciencetool',
            name='linkFirst',
            field=models.TextField(blank=True, default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='announcmentssciencetool',
            name='linkFirstName',
            field=models.CharField(blank=True, default=False, max_length=20),
        ),
        migrations.AddField(
            model_name='announcmentssciencetool',
            name='linkSecond',
            field=models.TextField(blank=True, default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='announcmentssciencetool',
            name='linkSecondName',
            field=models.CharField(blank=True, default=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='announcmentssciencetool',
            name='tags',
            field=models.TextField(blank=True, default=False, max_length=100),
        ),
    ]
