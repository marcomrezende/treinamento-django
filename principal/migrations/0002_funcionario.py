# Generated by Django 4.1.1 on 2022-09-27 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=104)),
                ('sexo', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMININO')], max_length=1)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cargo', models.ForeignKey(db_column='id_cargo', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.cargo')),
            ],
            options={
                'db_table': 'funcionario',
                'managed': True,
            },
        ),
    ]
