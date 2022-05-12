# Generated by Django 4.0.4 on 2022-05-12 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=55)),
                ('year_released', models.IntegerField()),
                ('number_of_players', models.IntegerField()),
                ('estimated_time_in_minutes', models.IntegerField()),
                ('age_recommendation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_body', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='GameRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=15)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.category')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(related_name='games', through='gamerraterapi.GameCategory', to='gamerraterapi.category'),
        ),
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.gamer'),
        ),
    ]
