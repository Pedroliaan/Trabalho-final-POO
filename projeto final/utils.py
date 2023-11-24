from classes.arquivo import Arquivo
from classes.carro import Carro


def registrar_carro():
    marca = input('insira a marca: ')
    modelo = input('insila o modelo: ')
    ano = int(input('insira o modelo: '))
    cor = input('insira a cor do veículo: ')
    preco = float(input('insira o preço: '))
    car = Carro(marca, modelo, ano, cor, preco)
    
    try:
        a = Arquivo('cadastro.txt', 'a')
        registro = a.abrir_arquivo()
        cadastro = (f'{car.get_marca()}; {car.get_modelo}; {car.get_ano}; {car.get_cor}; {car.get_preco}')
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
        a = open('agenda.txt','r', encoding='utf-8')
        a.close()
        return True
    except FileNotFoundError:
        print(f'Arquivo {arquivo} não existe :/')
        return False

def contar_registro() -> int:
    if verfica_existe_arquivo('cadastro.txt'):
        num_cadastros = 0
        with(open('agenda.txt', 'r', encoding='utf-8')) as cadastro:
            linhas = cadastro.readlines()

        for _ in linhas:
            num_cadastros += 1

        return num_cadastros
    else:
        print('\t\tNão existem contatos ...')
        return 0
