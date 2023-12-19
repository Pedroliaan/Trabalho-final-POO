import operacao

class Venda(operacao):
    def __init__(self,id_operacao,valor, parcelas, carro):
        super().__init__(id_operacao,valor, carro)
        self.parcelas = parcelas