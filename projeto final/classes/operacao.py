class Operacao:
    def __init__(self, id_operacao:int, valor:float, carro:str, tipo:str):
        self.__carro = carro
        self.__valor = valor
        self.__id_operacao = id_operacao
        self.__tipo = tipo
    
    def get_carro(self):
        return self.__carro
    def set_carro(self,carro):
        self.__carro = carro
    def get_valor(self):
        return self.__valor
    def set_valor(self, valor):
        self.__valor = valor
    def get_id_operacao(self):
        return self.__id_operacao
    def set_id_operacao(self, id_operacao):
        self.__id_operacao = id_operacao
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self,tipo):
        self.__tipo = tipo

class Venda(Operacao):
    def __init__(self,id_operacao,valor, parcelas, carro, tipo):
        super().__init__(id_operacao,valor, carro, tipo)
        self.__parcelas = parcelas
        
    def get_parcelas(self):
        return self.__parcelas
    def set_parcelas(self,parcelas):
        self.__parcelas = parcelas

class Aluguel(Operacao):
    def __init__(self,id_operacao,valor, dias, carro, tipo):
        super().__init__(id_operacao,valor, carro, tipo)
        self.__dias = dias
    
    def get_dias(self):
        return self.__dias
    def set_dias(self, dias):
        self.__dias = dias