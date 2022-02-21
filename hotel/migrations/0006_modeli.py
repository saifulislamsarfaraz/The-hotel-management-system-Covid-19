# Generated by Django 4.0.2 on 2022-02-20 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modeli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('category', models.CharField(choices=[('YAC', 'Ac'), ('NAC', 'Non-Ac'), ('DEL', 'Deluex'), ('KIN', 'King'), ('QUE', 'Queen'), ('STDIOU', 'Stduio'), ('HTR', 'Hollywood-Twin-Room'), ('ES', 'Executive'), ('MS', 'MiniSuite'), ('PS', 'PresidentialSuite'), ('AP', 'Apartments'), ('CR', 'ConnectingRooms'), ('MR', 'MurphyRooms'), ('AR', 'Accessible'), ('CN', 'Cabana'), ('ADR', 'AdjoiningRoom'), ('VIL', 'Villa'), ('EF', 'ExecutiveRoom'), ('NSM', 'Non-SmokingRoom')], max_length=6)),
                ('beds', models.IntegerField()),
                ('desc', models.TextField()),
                ('capacity', models.IntegerField()),
                ('image', models.CharField(max_length=400)),
            ],
        ),
    ]