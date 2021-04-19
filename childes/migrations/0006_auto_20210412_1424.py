# Generated by Django 3.0.6 on 2021-04-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childes', '0005_auto_20210412_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mother',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('corpus', models.CharField(max_length=200)),
                ('tot_utts', models.IntegerField(default=0)),
                ('mlu_utts', models.IntegerField(default=0)),
                ('mlu_words', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('mlu_morphs', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('freq_ttr', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('percent_nouns', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('percent_verbs', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('percent_adjs', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('percent_adv', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('percent_prep', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='freq_ttr_mot',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='mlu_morphs_mot',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='mlu_utts_mot',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='mlu_words_mot',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='percent_adjs_mot',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='percent_adv_mot',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='percent_nouns_mot',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='percent_prep_mot',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='percent_verbs_mot',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='tot_utts_mot',
        ),
    ]