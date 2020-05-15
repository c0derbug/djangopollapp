# Generated by Django 2.2.10 on 2020-05-15 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
            ],
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title of poll')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Poll start date')),
                ('end_date', models.DateTimeField(verbose_name='Poll end date')),
                ('description', models.TextField(verbose_name='Poll description')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Poll author')),
                ('members', models.ManyToManyField(blank=True, to='djangopollapp.ClientsID', verbose_name='Members')),
            ],
            options={
                'verbose_name': 'Poll',
                'verbose_name_plural': 'Polls',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qns', models.CharField(max_length=256, verbose_name='Question')),
                ('qns_type', models.IntegerField(choices=[(1, 'Text answer'), (2, 'Single choice'), (3, 'Multi choice')], default=3)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangopollapp.Polls')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Answer text')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangopollapp.ClientsID', verbose_name='Answer author')),
                ('qns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangopollapp.Questions')),
            ],
            options={
                'verbose_name': 'Text Answer',
                'verbose_name_plural': 'Text Answers',
            },
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256, verbose_name='Choice text')),
                ('qns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangopollapp.Questions')),
                ('votes', models.ManyToManyField(blank=True, to='djangopollapp.ClientsID', verbose_name='Votes')),
            ],
            options={
                'verbose_name': 'Choice text',
                'verbose_name_plural': 'Choice text',
            },
        ),
    ]