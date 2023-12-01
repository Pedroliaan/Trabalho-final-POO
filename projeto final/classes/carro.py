class Carro:
    def __init__(self, id:int, marca:str, modelo:str, ano:int, cor:str, preco:float):
        
        self.__id = id
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preco = preco
    
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def get_ano(self):
        return self.__ano
    def set_ano(self, ano):
        self.__ano = ano
    def get_cor(self):
        return self.__cor
    def set_cor(self, cor):
        self.__cor = cor
    def get_preco(self):
        return self.__preco
    def set_preco(self, preco):
        self.__preco = preco