# Generated by Django 4.0.2 on 2022-02-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_alter_room_category_alter_room_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.CharField(max_length=50)),
                ('number2', models.IntegerField()),
                ('number3', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('YAC', 'Ac'), ('NAC', 'Non-Ac'), ('DEL', 'Deluex'), ('KIN', 'King'), ('QUE', 'Queen'), ('STDIOU', 'Stduio'), ('HTR', 'Hollywood-Twin-Room'), ('ES', 'Executive'), ('MS', 'MiniSuite'), ('PS', 'PresidentialSuite'), ('AP', 'Apartments'), ('CR', 'ConnectingRooms'), ('MR', 'MurphyRooms'), ('AR', 'Accessible'), ('CN', 'Cabana'), ('ADR', 'AdjoiningRoom'), ('VIL', 'Villa'), ('EF', 'ExecutiveRoom'), ('NSM', 'Non-SmokingRoom')], max_length=6),
        ),
    ]
