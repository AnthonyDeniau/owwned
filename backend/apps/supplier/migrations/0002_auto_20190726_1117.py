# Generated by Django 2.2.3 on 2019-07-26 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='webStie',
            new_name='webSite',
        ),
    ]
