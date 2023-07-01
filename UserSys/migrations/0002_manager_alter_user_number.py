# Generated by Django 4.2.2 on 2023-07-01 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
