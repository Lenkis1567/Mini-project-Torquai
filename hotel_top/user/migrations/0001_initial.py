# Generated by Django 4.2.1 on 2023-05-12 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdultsCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('is_answered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('adults', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.adultscount')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_beginning', models.DateField()),
                ('date_end', models.DateField()),
                ('client', models.IntegerField(blank=True, null=True)),
                ('paid', models.BooleanField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.rooms')),
            ],
        ),
    ]
