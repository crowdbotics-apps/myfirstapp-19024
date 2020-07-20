# Generated by Django 2.2.14 on 2020-07-20 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat_user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('attachment', models.URLField()),
                ('is_draft', models.BooleanField()),
                ('is_delivered', models.BooleanField()),
                ('is_read', models.BooleanField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_delivered', models.DateTimeField()),
                ('timestamp_read', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('thread_photo', models.URLField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThreadMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField()),
                ('timestamp_joined', models.DateTimeField(auto_now_add=True)),
                ('timestamp_left', models.DateTimeField()),
                ('last_rejoined', models.DateTimeField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threadmember_profile', to='chat_user_profile.Profile')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threadmember_thread', to='chat.Thread')),
            ],
        ),
        migrations.CreateModel(
            name='ThreadAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=7)),
                ('timestamp_action', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threadaction_profile', to='chat_user_profile.Profile')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threadaction_thread', to='chat.Thread')),
            ],
        ),
        migrations.CreateModel(
            name='MessageAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=7)),
                ('timestamp_action', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messageaction_message', to='chat.Message')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messageaction_profile', to='chat_user_profile.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='sent_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sent_by', to='chat.ThreadMember'),
        ),
        migrations.AddField(
            model_name='message',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_thread', to='chat.Thread'),
        ),
        migrations.CreateModel(
            name='ForwardedMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_forwarded', models.DateTimeField(auto_now_add=True)),
                ('forwarded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forwardedmessage_forwarded_by', to='chat_user_profile.Profile')),
                ('forwarded_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forwardedmessage_forwarded_to', to='chat.Thread')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forwardedmessage_message', to='chat.Message')),
            ],
        ),
    ]
