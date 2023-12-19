import operacao

class Aluguel(operacao):
    def __init__(self,id_operacao,valor, dias, carro):
        super().__init__(id_operacao,valor, carro)
        self.dias = dias