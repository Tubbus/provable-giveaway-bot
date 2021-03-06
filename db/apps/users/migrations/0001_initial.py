# Generated by Django 2.2.2 on 2019-06-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_id', models.BigIntegerField()),
                ('name', models.CharField(blank=True, max_length=200)),
                ('discriminator', models.CharField(max_length=4)),
                ('logged_at', models.DateTimeField(auto_now_add=True)),
                ('user_seed', models.CharField(max_length=200)),
                ('server_seed', models.CharField(max_length=300)),
                ('nonce', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
