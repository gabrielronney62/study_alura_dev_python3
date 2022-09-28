
class conta():

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        conta.numero = numero
        conta.titular = titular
        conta.saldo = saldo
        conta.limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))


    def deposita(self, valor):
        self.saldo += valor


    def saca(self, valor):
        self.saldo -= valor