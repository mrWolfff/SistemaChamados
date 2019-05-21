# Generated by Django 2.0.13 on 2019-05-16 22:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaChamado', '0005_auto_20190516_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('admin', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='chamados',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='chamados',
            name='solucao',
            field=models.CharField(default='\t', max_length=250),
        ),
        migrations.AddField(
            model_name='chamados',
            name='status',
            field=models.CharField(default='Não Realizado', max_length=20),
        ),
        migrations.AddField(
            model_name='chamados',
            name='usuario',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]
