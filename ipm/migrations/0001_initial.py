# Generated by Django 2.2.5 on 2019-09-27 18:47

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
            name='Biblia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testamento', models.CharField(choices=[('Velho Testamento', 'Velho Testamento'), ('Novo Testamento', 'Novo Testamento')], max_length=255, verbose_name='Testamento')),
                ('livro', models.CharField(choices=[('Gênesis', 'Gênesis'), ('Êxodo', 'Êxodo'), ('Levítico', 'Levítico'), ('Números', 'Números'), ('Deuteronômio', 'Deuteronômio'), ('Josué', 'Josué'), ('Juízes', 'Juízes'), ('Rute', 'Rute'), ('1º Samuel', '1º Samuel'), ('2º Samuel', '2º Samuel'), ('1º Reis', '1º Reis'), ('2º Reis', '2º Reis'), ('1º Crônicas', '1º Crônicas'), ('2º Crônicas', '2º Crônicas'), ('Esdras', 'Esdras'), ('Neemias', 'Neemias'), ('Ester', 'Ester'), ('Jó', 'Jó'), ('Salmos', 'Salmos'), ('Provérbios', 'Provérbios'), ('Eclesiastes', 'Eclesiastes'), ('Cânticos', 'Cânticos'), ('Isaías', 'Isaías'), ('Jeremias', 'Jeremias'), ('Lamentações de Jeremias', 'Lamentações de Jeremias'), ('Ezequiel', 'Ezequiel'), ('Ezequiel', 'Ezequiel'), ('Oséias', 'Oséias'), ('Joel', 'Joel'), ('Amós', 'Amós'), ('Obadias', 'Obadias'), ('Jonas', 'Jonas'), ('Miquéias', 'Miquéias'), ('Naum', 'Naum'), ('Habacuque', 'Habacuque'), ('Sofonias', 'Sofonias'), ('Ageu', 'Ageu'), ('Zacarias', 'Zacarias'), ('Malaquias', 'Malaquias'), ('Mateus', 'Mateus'), ('Marcos', 'Marcos'), ('Lucas', 'Lucas'), ('João', 'João'), ('Atos', 'Atos'), ('Romanos', 'Romanos'), ('1ª Coríntios', '1ª Coríntios'), ('2ª Coríntios', '2ª Coríntios'), ('Gálatas', 'Gálatas'), ('Efésios', 'Efésios'), ('Filipenses', 'Filipenses'), ('Colossenses', 'Colossenses'), ('1ª Tessalonicenses', '1ª Tessalonicenses'), ('2ª Tessalonicenses', '2ª Tessalonicenses'), ('1ª Timóteo', '1ª Timóteo'), ('2ª Timóteo', '2ª Timóteo'), ('Tito', 'Tito'), ('Filemom', 'Filemom'), ('Hebreus', 'Hebreus'), ('Tiago', 'Tiago'), ('1ª Pedro', '1ª Pedro'), ('2ª Pedro', '2ª Pedro'), ('1ª João', '1ª João'), ('2ª João', '2ª João'), ('3ª João', '3ª João'), ('Judas', 'Judas'), ('Apocalipse', 'Apocalipse')], max_length=255, verbose_name='Livro')),
                ('version', models.CharField(max_length=255, verbose_name='Versão')),
                ('chapter', models.PositiveIntegerField(verbose_name='Capítulo')),
                ('verse', models.PositiveIntegerField(verbose_name='Verso')),
                ('text', models.TextField(verbose_name='Texto')),
            ],
        ),
        migrations.CreateModel(
            name='Estudos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('resumo', models.TextField(verbose_name='Resumo')),
                ('tags', models.CharField(choices=[('1', 'Avivamento'), ('2', 'Biografia'), ('3', 'Discipulado'), ('4', 'Evangelismo'), ('5', 'Família'), ('6', 'Ficção Cristã'), ('7', 'Geografía'), ('8', 'Gestão e Finanças'), ('9', 'História'), ('10', 'Igreja'), ('11', 'Libertação'), ('12', 'Liderança'), ('13', 'Oração'), ('14', 'Testemunho'), ('15', 'Vida Cristã')], max_length=30, verbose_name='Tags')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
