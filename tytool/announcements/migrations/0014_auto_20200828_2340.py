# Generated by Django 3.1 on 2020-08-28 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('announcements', '0013_announcmentssciencetool_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcmentssciencetool',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
