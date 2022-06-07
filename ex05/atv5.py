from funcoes import *

opcao = tipo_de_calculo()

while opcao != 3:
    print('---OPÇÃO INVALIDA---')

    opcao = tipo_de_calculo()

    if opcao == 1:
        area = opcao_1(opcao)
    elif opcao == 2:
        area = opcao_2(opcao)
    elif opcao == 3:
        area = opcao_3(opcao)

print(f'a area é {area:.1f}')