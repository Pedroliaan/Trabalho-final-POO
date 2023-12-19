import operacao

class Aluguel(operacao):
    def __init__(self,id_operacao,valor, dias, carro):
        super().__init__(id_operacao,valor, carro)
        self.__dias = dias
    
    def get_dias(self):
        return self.__dias
    def set_dias(self, dias):
        self.__dias = dias