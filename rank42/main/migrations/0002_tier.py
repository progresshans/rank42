# Generated by Django 2.2.7 on 2020-06-02 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('FtUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.FtUser')),
                ('coalition_point', models.IntegerField(blank=True, null=True, verbose_name='길드 포인트')),
                ('tier_name', models.CharField(blank=True, max_length=13, null=True)),
                ('tier_rank', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
