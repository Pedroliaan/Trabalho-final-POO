from classes.arquivo import Arquivo
from classes.carro import Carro
from classes.operacao import Venda
from classes.operacao import Aluguel


def registrar_carro():
    id = verifica_id()
    marca = input('insira a marca: ')
    modelo = input('insila o modelo: ')
    ano = int(input('insira o ano: '))
    cor = input('insira a cor do veículo: ')
    preco = float(input('insira o preço: '))
    car = Carro(id,marca, modelo, ano, cor, preco)
    
    try:
        a = Arquivo('cadastro.txt', 'a')
        registro = a.abrir_arquivo()
        cadastro = (f'{car.get_id()};{car.get_marca()}; {car.get_modelo()};' 
                    f'{car.get_ano()}; {car.get_cor()}; {car.get_preco()}\n')
        registro.write(cadastro)
        a.fechar_arquivo(registro)
    except FileNotFoundError: 
        print("arquivo não encontrado")
    except IOError:
        print('houve um problema na entrada dos dados')
    except Exception:
        ("ERRO!")
    else:
        print('Carro registrado com sucesso!')
          
def verfica_existe_arquivo(arquivo: str) -> bool:
    try:
        a = open('cadastro.txt','r', encoding='utf-8')
        a.close()
        return True
    except FileNotFoundError:
        print(f'Arquivo {arquivo} não existe')
        return False

def contar_cadastro() -> int:
    if verfica_existe_arquivo('cadastro.txt'):
        num_cadastros = 0
        with(open('cadastro.txt', 'r', encoding='utf-8')) as cadastro:
            linhas = cadastro.readlines()

        for _ in linhas:
            num_cadastros += 1

        return num_cadastros
    else:
        print('\t\tNão existem cadastros ...')
        return 0

def verifica_id():
    if contar_cadastro() > 0:
        a = open('cadastro.txt', 'r', encoding='utf-8')
        lista = a.readlines()
        aux = lista[-1]
        id_ant = aux.split(';')[0]
        return int(id_ant) + 1
    else:
         return 1 
    
def listar_registro():
    lista = open('cadastro.txt', 'r', encoding='utf-8')
    if contar_cadastro() > 0:
        print('\n\t\t Listar carros:')
        for carro in lista:
            exibe_registro(carro)
    else:
        print('\t\t NÃO EXISTEM CARROS REGISTRADOS')
    lista.close()
         
def exibe_registro(registro):
    print(
        f'Id:{registro.split(";")[0]} '
        f'Marca: {registro.split(";")[1]} '
        f'Modelo: {registro.split(";")[2]} '
        f'ano: {registro.split(";")[3]} '
        f'cor: {registro.split(";")[4]} '
        f'preco: {registro.split(";")[5]} '
        )

def deletar_registro(id_deletar=-1):
    if contar_cadastro() > 0:
        if id_deletar == -1:
            id_deletar = input('\t\tDigite o ID para ser deletado: ')
        else: id_deletar = id_deletar
        registro = open('cadastro.txt', 'r', encoding='utf-8')
        aux, aux2 = [], []
        
        for x in registro:
            aux.append(x)

        for x in range(0, len(aux)):
            id_temp = aux[x].split(";")[0]

            if id_deletar != id_temp:
                aux2.append(aux[x])
        registro.close()
        registro = open('cadastro.txt', 'w', encoding='utf-8')
        
        for x in aux2:
            registro.write(x)
        registro.close()
        
        print('\t\tCarro deletado dos registros com sucesso!')
    else:
        print('\t\tNão existem cadastros')
def atualizar_registro():
    if contar_cadastro() > 0:
        listar_registro()
        id = input('\t\tDigite o id do registro que será atualizado')
        deletar_registro(id)
        registro = open('cadastro.txt', 'r', encoding='utf-8')
        aux, aux2 = [], []
        for x in registro:
            aux.append(x)

        for x in range(0, len(aux)):
            id_temp = aux[x].split(";")[0]

            if id != id_temp:
                aux2.append(aux[x])
        registro.close()
        registro = open('cadastro.txt', 'w', encoding='utf-8')
        
        for x in aux2:
            registro.write(x)
        registro.close()
        
        id = id 
        marca = input('\t\tInsira o novo nome da marca:')
        modelo = input('\t\tInsira o novo nome do modelo:')
        ano = input('\t\tInsira o novo ano:')
        cor = input('\t\tInsira o novo nome da cor:')
        preco = input('\t\tInsira o novo preço:')
        
        try:
            registro = open('cadastro.txt', 'a', encoding='utf-8')
            dados = f'{id};{marca};{modelo};{ano};{cor};{preco}'
            registro.write(dados)
            registro.close()
            print('\t\tRegistro atualizado')
        except FileNotFoundError:
            print('\t\tERRO AO SALVAR CONTATO!')
    else:
        print('\t\t Não existem registros')
def resetar_arquivo():
    try:
        with(open('cadastro.txt', 'w', encoding='utf-8')) as a:
            pass
    except Exception:
        print(f'Um erro ocorreu')
    else:
        print(f'\t\tArquivo deletado com sucesso')

def calcula_parcela(id:str, parcelas:int):
    try:
       v = calcula_valor(id)
       return f'{parcelas}x de {v/parcelas}'

    except Exception:
        print('erro no calculo de parcelas')
def contar_operacoes():
    if verfica_existe_arquivo('operacoes.txt'):
        num_operacoes = 0
        with(open('operacoes.txt', 'r', encoding='utf-8')) as operacoes:
            linhas = operacoes.readlines()

        for _ in linhas:
            num_operacoes += 1

        return num_operacoes
    else:
        print('\t\tNão existem simulações ...')
        return 0
def calcula_valor(id):
    a = open('cadastro.txt', 'r', encoding='utf-8')
    linhas = a.readlines()
    for x in range(len(linhas)):
        if linhas[x].startswith(id):
            new = [linhas[x]]
            view = [new[0].split(';')]
            v = view[0][5].strip('\n')
            return float(v)
        else:
            pass
def seleciona_carro(id:str):
    a = open('cadastro.txt', 'r', encoding='utf-8')
    linhas = a.readlines()
    for x in range(len(linhas)):
        if linhas[x].startswith(id):
            new = [linhas[x]]
            return new[0]
        else:
            pass
def simula_venda():
    listar_registro()
    i = input('Insira o id do carro que você deseja vender:')
    p = int(input('insira a quantidade das parcelas que você deseja:'))
    id = contar_operacoes() + 1
    valor = calcula_valor(i)
    parcelas = calcula_parcela(i,p)
    car = seleciona_carro(i).strip('\n')
    carro = car.strip('\n')
    tipo = 'venda'
    v = Venda(id,valor,parcelas,carro, tipo)    
    
    try:
        a = Arquivo('operacoes.txt', 'a')
        registro = a.abrir_arquivo()
        operacao = (f'{v.get_id_operacao()};{v.get_valor()}; {v.get_parcelas()};' 
                    f'{v.get_carro()}; {v.get_tipo()}\n')
        registro.write(operacao)
        a.fechar_arquivo(registro)
        exibe_operacao(operacao)
        deletar_registro(i)
    except FileNotFoundError: 
        print("arquivo não encontrado")
    except IOError:
        print('houve um problema na entrada dos dados')
    except Exception:
        ("ERRO!")
    else:
        pass
    
def simula_aluguel():
    listar_registro()
    i = input('Insira o id do carro que você deseja simular o aluguel:')
    p = int(input('insira a quantidade de dias que você deseja alugar:'))
    id = contar_operacoes() + 1
    carro = seleciona_carro(i).strip('\n')
    tipo = 'aluguel'
    valor = calcula_aluguel(i,p)
    alu = Aluguel(id,valor,p,carro,tipo)
    
    try: 
        a = Arquivo('operacoes.txt', 'a')
        registro = a.abrir_arquivo()
        operacao =(f'{alu.get_id_operacao()};{alu.get_valor()}; {alu.get_dias()};' 
                    f'{alu.get_carro()}; {alu.get_tipo()}\n')
        registro.write(operacao)
        a.fechar_arquivo(registro)
        exibe_operacao(operacao)
        
    except FileNotFoundError: 
     print("arquivo não encontrado")
    except IOError:
        print('houve um problema na entrada dos dados')
    except Exception:
        ("ERRO!")
    else:
        pass

def calcula_aluguel(id, dias):
    try:
        v = calcula_valor(id)
        if v > 100000:
            return f'Aluguel de {dias} dias, 35 R$ por dia. total {35*dias}R$'
        elif v > 500000:
            return f'Aluguel de {dias} dias, 65 R$ por dia. total {65*dias}R$'
        elif v > 1000000:
            return f'Aluguel de {dias} dias, 150 R$ por dia. total {150*dias}R$'
        else: 
            return f'Aluguel de {dias} dias, 25 R$ por dia. total {25*dias}R$'
        
    except Exception:
        print("erro no calculo de diarias")

def exibe_operacao(lista):
    tip = lista.split(";")[9].strip("\n")
    if tip == ' aluguel':
        print(
        f' id: {lista.split(";")[0]}'
        f' valor: {lista.split(";")[1]}'
        f' dias: {lista.split(";")[2]}'
        f' carro: {lista.split(";")[4]} {lista.split(";")[5]} {lista.split(";")[6]} {lista.split(";")[7]}'
        f' tipo: {tip}')
    elif tip == " venda":
        print(
        f' id: {lista.split(";")[0]}'
        f' valor: {lista.split(";")[1]}'
        f' parcelas: {lista.split(";")[2]}'
        f' carro: {lista.split(";")[4]} {lista.split(";")[5]} {lista.split(";")[6]} {lista.split(";")[7]}'
        f' tipo: {tip}'
        )
    
def listar_operacoes():
    lista = open('operacoes.txt', 'r', encoding='utf-8')
    if contar_operacoes() > 0:
        print('\n\t\t Listar operações: ')
        for operacao in lista:
            exibe_operacao(operacao)
    else:
        print("\t\t NÃO EXISTEM OPERACOES CADASTRADOS")
    lista.close()