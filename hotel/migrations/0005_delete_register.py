# Generated by Django 4.0.2 on 2022-02-20 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_register_alter_room_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
    ]