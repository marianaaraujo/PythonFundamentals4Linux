import requests

class Empregado:
    fator_aumento = 1.05

    def __init__(self, primeiro_nome, ultimo_nome, pagamento):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.pagamento = pagamento

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.primeiro_nome, self.ultimo_nome)

    @property
    def nome_completo(self):
        return '{} {}'.format(self.primeiro_nome, self.ultimo_nome)

    def aplica_aumento(self):
        self.pagamento = int(self.pagamento * self.fator_aumento)

    def agenda_mensal(self, mes):
        response = requests.get('http://company.com/{}/{}'.format(self.ultimo_nome, mes))

        if response.ok:
            return response.text
        else:
            return 'Falha na requisição!'


