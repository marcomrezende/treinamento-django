# Generated by Django 4.1.1 on 2022-09-27 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=104)),
            ],
            options={
                'db_table': 'cargo',
                'managed': True,
            },
        ),
    ]
