# Generated by Django 2.0.13 on 2019-05-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaChamado', '0003_auto_20190515_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamados',
            name='descricao',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='chamados',
            name='prioridade',
            field=models.CharField(max_length=200),
        ),
    ]