class Caixa:
    def __init__(self):
        self.valor_limite = float(500.00)
        self.operacao_limite = int(3)
        self.saldo = float(0.00)
        self.extrato = []


    def depositar(self, valor):
        valor = self.valor_format(valor)
        if valor > 0:
            self.saldo += valor
            self.extrato.append('Deposito: R$' + str(valor))
            print('Deposito realizado com sucesso!')
        else:
            print('Valor invalido!')


    def sacar(self, valor):
        valor = self.valor_format(valor)
        if self.check_limite_valor(valor) and self.check_limite_operacao() and self.check_saldo(valor):
            self.saldo -= valor
            self.operacao_limite -= int(1)
            self.extrato.append('Saque: R$' + str(valor))
            print('Saque realizado com sucesso!')


    def exibir_extrato(self):
        print('Extrato')
        for i in self.extrato:
            print(i)
        print('Saldo: R$' + str(self.saldo))
        print('Valor limite: R$' + str(self.valor_limite))
        print('Limite de operacoes: ' + str(self.operacao_limite))


    def valor_format(self, valor):
        if ',' in valor:
            valor = valor.replace(',', '.')
        return float(valor)


    def check_limite_valor(self, valor):
        if valor > self.valor_limite:
            print('Valor acima do limite!')
            return False
        return True


    def check_limite_operacao(self):
        if self.operacao_limite == 0:
            print('Limite de operacoes atingido!')
            return False
        return True


    def check_saldo(self, valor):
        if self.saldo <= valor:
            print('Saldo insuficiente!')
            return False
        return True
