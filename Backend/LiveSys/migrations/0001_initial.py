# Generated by Django 4.2.2 on 2023-07-01 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Liveroom',
            fields=[
                ('roomID', models.AutoField(primary_key=True, serialize=False, verbose_name='roomID')),
                ('roomName', models.CharField(max_length=100, verbose_name='roomName')),
                ('roomInfo', models.CharField(max_length=2048, verbose_name='roomInfo')),
            ],
            options={
                'db_table': '直播间表',
            },
        ),
        migrations.CreateModel(
            name='RelationbUandL',
            fields=[
                ('RID', models.AutoField(primary_key=True, serialize=False, verbose_name='RID')),
                ('isManager', models.BooleanField(default=False, verbose_name='isManager')),
                ('isProhibited', models.BooleanField(default=False, verbose_name='isProhibited')),
                ('FLiveroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LiveSys.liveroom', verbose_name='FLiveroom')),
            ],
            options={
                'db_table': '用户与直播间关系表',
            },
        ),
    ]
