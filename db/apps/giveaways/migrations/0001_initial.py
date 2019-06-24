# Generated by Django 2.2.2 on 2019-06-24 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('guilds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Giveaway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize', models.CharField(max_length=200)),
                ('winner_count', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ended_at', models.DateTimeField()),
                ('ended_time_str', models.CharField(max_length=200)),
                ('success', models.BooleanField(help_text='• Checked: Giveaway happened successfully.<br/>• Unchecked: Giveaway failed due to a Discord exception.<br/>• None: Giveaway happening.', null=True)),
                ('channel_id', models.BigIntegerField(blank=True, null=True)),
                ('message_id', models.BigIntegerField(blank=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giveaways', to='users.DiscordUser')),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giveaways', to='guilds.DiscordGuild')),
                ('participants', models.ManyToManyField(blank=True, null=True, related_name='_giveaway_participants_+', to='users.DiscordUser')),
                ('winners', models.ManyToManyField(blank=True, null=True, related_name='_giveaway_winners_+', to='users.DiscordUser')),
            ],
        ),
    ]
