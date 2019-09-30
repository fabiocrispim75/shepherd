from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import get_user_model

class Cidade(models.Model):
    nome = models.CharField(max_length=255, verbose_name ='Nome')
    estado = models.CharField(max_length=10, verbose_name ='Estado')
    capital = models.CharField(max_length=1, verbose_name ='Capital')

    def __str__(self):
        return self.nome

class Igreja(models.Model):
    UF = (
        ('Acre', 'AC'),
        ('Alago', 'AL'), 
        ('Amazo', 'AM'),
        ('Amapa', 'AP'),
        ('Bahia', 'BA'),
        ('Ceara', 'CE'),
        ('Dist', 'DF'),
        ('Espi', 'ES'),
        ('Goias', 'GO'),
        ('Maran', 'MA'),
        ('Matog', 'MT'),
        ('Matos', 'MS'),
        ('Minas', 'MG'),
        ('Para', 'PA'),
        ('Parai', 'PB'),
        ('Paran', 'PR'),
        ('Perna', 'PE'),
        ('Piaui', 'PI'),
        ('Rio', 'RJ'),
        ('Rion', 'RN'),
        ('Rios', 'RS'),
        ('Rondo', 'RO'),
        ('Rora', 'RR'),
        ('Santa', 'SC'),
        ('Sao', 'SP'),
        ('Ser', 'SE'),
        ('Toca', 'TO'),
    )

    STATUS = (
        ('sim', 'SIM'),
        ('nao', 'NÃO'), 
    )
    nome = models.CharField(max_length=255, verbose_name ='Igreja')
    CNPJ = models.CharField(max_length=255, verbose_name ='CNPJ')
    endereco = models.CharField(max_length=255, verbose_name ='Endereço')
    numero = models.CharField(max_length=255, verbose_name ='Número')
    estado = models.CharField(max_length=255,choices=UF, verbose_name = 'Estado')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name = 'Cidade')
    telefone = models.CharField(max_length=100, verbose_name ='Telefone fixo')
    celular = models.CharField(max_length=100, verbose_name ='Celular')
    responsavel = models.CharField(max_length=100, verbose_name ='Nome responsável')
    cpf = models.CharField(max_length=14, verbose_name ='CPF') 
    ativo = models.CharField(max_length=255,choices=STATUS, verbose_name = 'Ativo')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Biblia(models.Model):

    TESTAMENTO = (
        ('Velho Testamento', 'Velho Testamento'),
        ('Novo Testamento', 'Novo Testamento'),
    )
    LIVRO = (
        ('Gênesis','Gênesis'),
        ('Êxodo','Êxodo'),
        ('Levítico','Levítico'),
        ('Números','Números'),
        ('Deuteronômio','Deuteronômio'),
        ('Josué','Josué'),
        ('Juízes','Juízes'),
        ('Rute','Rute'),
        ('1º Samuel','1º Samuel'),
        ('2º Samuel','2º Samuel'),
        ('1º Reis','1º Reis'),
        ('2º Reis','2º Reis'),
        ('1º Crônicas','1º Crônicas'),
        ('2º Crônicas','2º Crônicas'),
        ('Esdras','Esdras'),
        ('Neemias','Neemias'),
        ('Ester','Ester'),
        ('Jó','Jó'),
        ('Salmos','Salmos'),
        ('Provérbios','Provérbios'),
        ('Eclesiastes','Eclesiastes'),
        ('Cânticos','Cânticos'),
        ('Isaías','Isaías'),
        ('Jeremias','Jeremias'),
        ('Lamentações de Jeremias','Lamentações de Jeremias'),
        ('Ezequiel','Ezequiel'),
        ('Ezequiel','Ezequiel'),
        ('Oséias','Oséias'),
        ('Joel','Joel'),
        ('Amós','Amós'),
        ('Obadias','Obadias'),
        ('Jonas','Jonas'),
        ('Miquéias','Miquéias'),
        ('Naum','Naum'),
        ('Habacuque','Habacuque'),
        ('Sofonias','Sofonias'),
        ('Ageu','Ageu'),
        ('Zacarias','Zacarias'),
        ('Malaquias','Malaquias'),
        ('Mateus','Mateus'),
        ('Marcos','Marcos'),
        ('Lucas','Lucas'),
        ('João','João'),
        ('Atos','Atos'),
        ('Romanos','Romanos'),
        ('1ª Coríntios','1ª Coríntios'),
        ('2ª Coríntios','2ª Coríntios'),
        ('Gálatas','Gálatas'),
        ('Efésios','Efésios'),
        ('Filipenses','Filipenses'),
        ('Colossenses','Colossenses'),
        ('1ª Tessalonicenses','1ª Tessalonicenses'),
        ('2ª Tessalonicenses','2ª Tessalonicenses'),
        ('1ª Timóteo','1ª Timóteo'),
        ('2ª Timóteo','2ª Timóteo'),
        ('Tito','Tito'),
        ('Filemom','Filemom'),
        ('Hebreus','Hebreus'),
        ('Tiago','Tiago'),
        ('1ª Pedro','1ª Pedro'),
        ('2ª Pedro','2ª Pedro'),
        ('1ª João','1ª João'),
        ('2ª João','2ª João'),
        ('3ª João','3ª João'),
        ('Judas','Judas'),
        ('Apocalipse','Apocalipse'),

    )
    testamento = models.CharField(max_length=255,choices=TESTAMENTO, verbose_name = 'Testamento')
    livro = models.CharField(max_length=255,choices=LIVRO, verbose_name = 'Livro')
    version = models.CharField(max_length=255, verbose_name ='Versão')
    chapter = models.PositiveIntegerField(verbose_name='Capítulo')
    verse = models.PositiveIntegerField(verbose_name='Verso')
    text = models.TextField(verbose_name='Texto')
    
    def __str__(self):
       return '{} em {} capítulo {} versículo {}'.format(self.testamento, self.livro, self.chapter, self.verse)


class Estudos(models.Model):

    ESTUDO = (
        ("1" , "Avivamento"),
        ("2" , "Biografia"), 
        ("3" , "Discipulado"),
        ("4" , "Evangelismo"),
        ("5" , "Família"),
        ("6" , "Ficção Cristã"),
        ("7" , "Geografía"),
        ("8" , "Gestão e Finanças"),
        ("9" , "História"),
        ("10" , "Igreja"),
        ("11" , "Libertação"),
        ("12" , "Liderança"),
        ("13" , "Oração"),
        ("14" , "Testemunho"),
        ("15" , "Vida Cristã"),

    )
    titulo = models.CharField(max_length=255, verbose_name = 'Título')
    resumo = models.TextField(verbose_name='Resumo')
    tags = models.CharField(max_length=30, choices=ESTUDO, verbose_name = 'Tags')
    texto = models.TextField(verbose_name='Texto')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Pregador(models.Model):
    ESTUDO = (
        ("1" , "Avivamento"),
        ("2" , "Biografia"), 
        ("3" , "Discipulado"),
        ("4" , "Evangelismo"),
        ("5" , "Família"),
        ("6" , "Ficção Cristã"),
        ("7" , "Geografía"),
        ("8" , "Gestão e Finanças"),
        ("9" , "História"),
        ("10" , "Igreja"),
        ("11" , "Libertação"),
        ("12" , "Liderança"),
        ("13" , "Oração"),
        ("14" , "Testemunho"),
        ("15" , "Vida Cristã"),

    )
    assunto = models.CharField(max_length=255, verbose_name = 'Título')
    resumo = models.TextField(verbose_name='Resumo')
    tags = models.CharField(max_length=30, choices=ESTUDO, verbose_name = 'Tags')
    texto = models.TextField(verbose_name='Texto')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.assunto

class Escola(models.Model):
    ESTUDO = (
        ("1" , "Avivamento"),
        ("2" , "Biografia"), 
        ("3" , "Discipulado"),
        ("4" , "Evangelismo"),
        ("5" , "Família"),
        ("6" , "Ficção Cristã"),
        ("7" , "Geografía"),
        ("8" , "Gestão e Finanças"),
        ("9" , "História"),
        ("10" , "Igreja"),
        ("11" , "Libertação"),
        ("12" , "Liderança"),
        ("13" , "Oração"),
        ("14" , "Testemunho"),
        ("15" , "Vida Cristã"),

    )
    titulo = models.CharField(max_length=255, verbose_name = 'Título')
    resumo = models.TextField(verbose_name='Resumo')
    tags = models.CharField(max_length=30, choices=ESTUDO, verbose_name = 'Tags')
    texto = models.TextField(verbose_name='Texto')
    media = models.FileField(upload_to='uploads/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo







