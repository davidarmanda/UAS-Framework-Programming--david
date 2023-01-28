# Generated by Django 2.2.12 on 2022-10-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20221025_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pembeli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_beli', models.CharField(default='BRG', max_length=8)),
                ('nama_pembeli', models.CharField(max_length=50)),
                ('harga', models.BigIntegerField()),
                ('link_gbr', models.CharField(blank=True, max_length=150)),
                ('waktu_posting', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
