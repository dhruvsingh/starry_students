# Generated by Django 3.0.8 on 2020-07-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False, help_text='The time this object was created.')),
                ('updated_at', models.DateTimeField(blank=True, help_text='The time this object was updated.', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]