# Generated by Django 4.2.1 on 2023-05-12 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_rommphoto_room'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RommPhoto',
            new_name='RoomPhoto',
        ),
    ]
