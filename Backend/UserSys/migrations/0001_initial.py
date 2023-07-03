# Generated by Django 3.2.11 on 2023-07-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_ID', models.AutoField(primary_key=True, serialize=False)),
                ('NickName', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Signature', models.CharField(blank=True, default='What your love is your life.', max_length=64)),
                ('Phone_number', models.CharField(blank=True, max_length=17)),
                ('Profile_photo', models.ImageField(default='defaultimgs/dfpp.jpg', upload_to='profile_photos/')),
                ('Register_time', models.DateTimeField()),
                ('Background_photo', models.ImageField(blank=True, upload_to='background_photos/')),
                ('Title', models.CharField(choices=[('mmww', '默默无闻'), ('wlzx', '未来之星'), ('hhym', '赫赫有名')], default='mmww', max_length=20)),
            ],
        ),
    ]
