# Generated by Django 2.2.5 on 2019-09-27 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipm', '0003_escola'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Igreja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Igreja')),
                ('CNPJ', models.CharField(max_length=255, verbose_name='CNPJ')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('numero', models.CharField(max_length=255, verbose_name='Número')),
                ('estado', models.CharField(choices=[('Acre', 'AC'), ('Alago', 'AL'), ('Amazo', 'AM'), ('Amapa', 'AP'), ('Bahia', 'BA'), ('Ceara', 'CE'), ('Dist', 'DF'), ('Espi', 'ES'), ('Goias', 'GO'), ('Maran', 'MA'), ('Matog', 'MT'), ('Matos', 'MS'), ('Minas', 'MG'), ('Para', 'PA'), ('Parai', 'PB'), ('Paran', 'PR'), ('Perna', 'PE'), ('Piaui', 'PI'), ('Rio', 'RJ'), ('Rion', 'RN'), ('Rios', 'RS'), ('Rondo', 'RO'), ('Rora', 'RR'), ('Santa', 'SC'), ('Sao', 'SP'), ('Ser', 'SE'), ('Toca', 'TO')], max_length=255, verbose_name='Estado')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone fixo')),
                ('celular', models.CharField(max_length=100, verbose_name='Celular')),
                ('responsavel', models.CharField(max_length=100, verbose_name='Nome responsável')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('ativo', models.CharField(choices=[('sim', 'SIM'), ('nao', 'NÃO')], max_length=255, verbose_name='Ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipm.Cidade', verbose_name='Cidade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]