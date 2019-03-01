# Generated by Django 2.1.7 on 2019-03-01 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ac_admin', '0001_initial'),
        ('ac_login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='citizenRegister',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('contact_number', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='citizen/')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_login.login')),
            ],
        ),
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('image', models.ImageField(upload_to='complaints/')),
                ('registration_date', models.DateField()),
                ('status', models.CharField(max_length=15)),
                ('closing_date', models.DateField()),
                ('ctid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_citizen.citizenRegister')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_admin.department')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('fid', models.IntegerField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('image', models.ImageField(upload_to='feedback/')),
                ('cid', models.ForeignKey(on_delete=True, to='ac_citizen.complaints')),
                ('ctid', models.ForeignKey(on_delete=True, to='ac_citizen.citizenRegister')),
            ],
        ),
    ]
