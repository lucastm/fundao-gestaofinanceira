from django.db import models

# Create your models here.
class Usuario(models.Model):
    CLIENTE = 'CLI'
    INTEGRADOR = 'INT'
    FORNECEDOR = 'FOR'
    TIPO = ((CLIENTE, 'Cliente'),
            (INTEGRADOR, 'Integrador'),
            (FORNECEDOR, 'Fornecedor'),
            )

    nome = models.CharField(max_length=70)
    tipo = models.CharField(max_length=3, choices=TIPO)
    cpfCnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + ' - ' + self.cpfCnpj

class Servico(models.Model):
    INTEGRACAO = 'INT'
    FORNECIMENTO = 'FOR'
    TIPO = ((INTEGRACAO, 'Integração'),
            (FORNECIMENTO, 'Fornecimento'),
            )

    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=3, choices=TIPO)
    valor = models.FloatField()
    dataContratacao = models.DateField()
    dataRealizacao = models.DateField()
    contratante = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='contratante')
    contratado = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='contratado')

    def __str__(self):
        return self.titulo

class Pagamento(models.Model):
    SERVICO = 'SER'
    TARIFACAO = 'TAR'
    TIPO = ((SERVICO, 'Serviço'),
            (TARIFACAO, 'Tarifação'),
            )

    JANEIRO = 1
    FEVEREIRO = 2
    MARCO = 3
    ABRIL = 4
    MAIO = 5
    JUNHO = 6
    JULHO = 7
    AGOSTO = 8
    SETEMBRO = 9
    OUTUBRO = 10
    NOVEMBRO = 11
    DEZEMBRO = 12
    MES = ((JANEIRO, 'Janeiro'),
           (FEVEREIRO, 'Fevereiro'),
           (MARCO, 'Março'),
           (ABRIL, 'Abril'),
           (MAIO, 'Maio'),
           (JUNHO, 'Junho'),
           (JULHO, 'Julho'),
           (AGOSTO, 'Agosto'),
           (SETEMBRO, 'Setembro'),
           (OUTUBRO, 'Outubro'),
           (NOVEMBRO, 'Novembro'),
           (DEZEMBRO, 'Dezembro'),
           )

    CRIADO = 'CRI'
    COBRADO = 'COB'
    BOLETO_GERADO = 'BOL_GER'
    PAGAMENTO_INFORMADO = 'PAG_INF'
    PAGAMENTO_CONFIRMADO = 'PAG_CONF'
    ESTADO = ((CRIADO, 'Criado'),
              (COBRADO, 'Cobrado'),
              (BOLETO_GERADO, 'Boleto gerado'),
              (PAGAMENTO_INFORMADO, 'Pagamento informado'),
              (PAGAMENTO_CONFIRMADO, 'Pagamento confirmado'),
              )

    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO)
    valorTotal = models.FloatField()
    subTotalImpostos = models.FloatField(null=True, blank=True)
    subTotalServicos = models.FloatField(null=True, blank=True)
    subTotalTarifacao = models.FloatField(null=True, blank=True)
    mes = models.IntegerField(choices=MES, null=True, blank=True)
    ano = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=8, choices=ESTADO)
    usuarioPagador = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='usuarioPagador')
    usuarioPago = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='usuarioPago', null=True, blank=True)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Andamento(models.Model):
    CRIADO = 'CRI'
    COBRADO = 'COB'
    BOLETO_GERADO = 'BOL_GER'
    PAGAMENTO_INFORMADO = 'PAG_INF'
    PAGAMENTO_CONFIRMADO = 'PAG_CONF'
    ESTADO = ((CRIADO, 'Criado'),
              (COBRADO, 'Cobrado'),
              (BOLETO_GERADO, 'Boleto gerado'),
              (PAGAMENTO_INFORMADO, 'Pagamento informado'),
              (PAGAMENTO_CONFIRMADO, 'Pagamento confirmado'),
              )

    dataAndamento = models.DateField()
    estado = models.CharField(max_length=8, choices=ESTADO)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.dataAndamento) + ' - ' + self.estado + ' - ' + self.pagamento.titulo

class UsoModulo(models.Model):
    SERVICOS = 'SERV'
    CONTRATOS = 'CONT'
    ORCAMENTOS = 'ORC'
    PAGAMENTOS = 'PAG'
    FATURAMENTOS = 'FAT'
    AFILIACAO = 'AFIL'
    AVALIACAO = 'AVAL'
    GESTAO_SERVICOS = 'GEST_SERV'
    GESTAO_CONTRATOS = 'GEST_CONT'
    GESTAO_ORCAMENTOS = 'GEST_ORC'
    GESTAO_FINANCEIRA = 'GEST_FIN'
    GESTAO_AFILIACAO = 'GEST_AFIL'
    GESTAO_AVALIACAO = 'GEST_AVAL'
    BI_SERVICOS = 'BI_SERV'
    BI_CONTRATOS = 'BI_CONT'
    BI_FINANCEIRA = 'BI_FIN'
    BI_AFILIACAO = 'BI_AFIL'
    BI_AVALIACAO = 'BI_AVAL'
    MODULO = ((SERVICOS, 'Serviços'),
              (CONTRATOS, 'Contratos'),
              (ORCAMENTOS, 'Orçamentos'),
              (PAGAMENTOS, 'Pagamentos'),
              (FATURAMENTOS, 'Faturamentos'),
              (AFILIACAO, 'Afiliação'),
              (AVALIACAO, 'Avaliação'),
              (GESTAO_SERVICOS, 'Gestão de serviços'),
              (GESTAO_CONTRATOS, 'Gestão de contratos'),
              (GESTAO_ORCAMENTOS, 'Gestão de orçamentos'),
              (GESTAO_FINANCEIRA, 'Gestão financeira'),
              (GESTAO_AFILIACAO, 'Gestão de afiliação'),
              (GESTAO_AVALIACAO, 'Gestão de avaliação'),
              (BI_SERVICOS, 'BI de serviço'),
              (BI_CONTRATOS, 'BI de contratos'),
              (BI_FINANCEIRA, 'BI financeiro'),
              (BI_AFILIACAO, 'BI de afiliação'),
              (BI_AVALIACAO, 'BI de avaliação'),
              )

    modulo = models.CharField(max_length=9, choices=MODULO)
    dataHoraInicio = models.DateTimeField()
    dataHoraFim = models.DateTimeField()
    duracao = models.FloatField()
    numTransações = models.IntegerField()

    def __str__(self):
        return self.modulo + ' - ' + str(self.dataHoraInicio) + ' - ' + str(self.dataHoraFim)





