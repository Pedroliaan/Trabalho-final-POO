from utils import registrar_carro
from utils import contar_cadastro
from utils import listar_registro
from utils import deletar_registro
from utils import atualizar_registro
from utils import resetar_arquivo

def menu():
    while True:
        print('                       ____________________                              ')
        print('                     //|           |        \                            ')
        print('                   //  |           |          \                          ')
        print('      ___________//____|___________|__________()\__________________      ')
        print('    /__________________|_=_________|_=___________|_________________{}    ')
        print('    [           ______ |           | .           | ==  ______      { }   ')
        print('  __[__        /##  ##\|           |             |    /##  ##\    _{# }_ ')
        print(' {_____)______|##    ##|___________|_____________|___|##    ##|__(______}')
        print('             /  ##__##                              /  ##__##        \   ')
        print('  _____         _              _____                         ')
        print(' |  __ \       | |            / ____|                        ')
        print(' | |__) |__  __| |_ __ ___   | |     __ _ _ __ _ __ ___  ___ ')
        print(" |  ___/ _ \/ _` | '__/ _ \  | |    / _` | '__| '__/ _ \/ __|")
        print(' | |  |  __/ (_| | | | (_) | | |___| (_| | |  | | | (_) \__ |')
        print(" |_|   \___|\__,_|_|  \___/   \_____\__,_|_|  |_|  \___/|___/")
        
        opcao = input(f'''
        {'=' * 64}
        MENU
        CARROS CADASTRADOS: {contar_cadastro()}

        [1] CADASTRAR CARRO       \t[4] ATUALIZAR REGISTRO
        [2] LISTAR CARROS          \t[5] RESETAR ARQUIVO
        [3] DELETAR REGISTRO DO CARRO         \t[0] SAIR
        {'=' * 64}

        ESCOLHA UMA OPÇÃO: ''')

        if opcao == '1':
            registrar_carro()
        elif opcao == '2':
            listar_registro()
        elif opcao == '3':
            deletar_registro()
        elif opcao == '4':
            atualizar_registro()
        elif opcao == '5':
            resetar_arquivo()
        elif opcao == '0':
            break
        else:
            print("opção inválida")
        
if __name__ == '__main__':
    menu()
    