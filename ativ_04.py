import os

def ativ02():
    print('\nOlá seja bem vindo a atividade 04, vamos precisar da coordenada de X:')
    
    try:
        codx = input()
        cod_X = float(codx.replace(',', '.'))
    except ValueError:
        print("Você não digitou um número válido.")
        reiniciar_app()

    try:
        print('\nAgora vamos precisar da coordenada de Y:')
        cody = input()
        cod_Y = float(cody.replace(',', '.'))
    except ValueError:
        print("Você não digitou um número válido.")
        reiniciar_app()

    if cod_X > 0 and cod_Y > 0:
        print(f'\nAs coordenadas de X {cod_X} e Y {cod_Y}, se encontram no Primeiro Quadrante')
        reiniciar_app()
    elif cod_X < 0 and cod_Y > 0:
        print(f'\nAs coordenadas de X {cod_X} e Y {cod_Y}, se encontram no Segundo Quadrante')
        reiniciar_app()
    elif cod_X < 0 and cod_Y < 0:
        print(f'\nAs coordenadas de X {cod_X} e Y {cod_Y}, se encontram no Terceiro Quadrante')
        reiniciar_app()
    elif cod_X > 0 and cod_Y < 0:
        print(f'\nAs coordenadas de X {cod_X} e Y {cod_Y}, se encontram no Quarto Quadrante')
        reiniciar_app()
    elif cod_X == 0 and cod_Y == 0:
        print(f'\nO ponto está localizado no eixo ou origem')
        reiniciar_app()
    else:
        print(f'\nValor inválido')
        reiniciar_app()

def reiniciar_app():

    print(f'\nDigite R para continuar ou qualquer tecla para finalizar.')
    reiniciar = input()
    escolha = reiniciar.upper()

    if escolha == 'R':
        os.system('cls')
        ativ02()
    else:
        finalizar_app()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')
    
def main():
    os.system('cls')
    ativ02()

if __name__ == '__main__':
    main()