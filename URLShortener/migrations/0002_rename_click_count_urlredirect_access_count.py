# Generated by Django 4.0.4 on 2022-05-29 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('URLShortener', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlredirect',
            old_name='click_count',
            new_name='access_count',
        ),
    ]
