import os

def ativ02():
    print('\nOlá seja bem vindo a atividade 02, qual é o seu nome?')
    nome = input()

    print(f'\n{nome} quantos anos você tem?')
    idade = int(input())

    if idade >= 0 and idade <= 12:
        print(f'\n{nome} você tem {idade} anos, logo você é criança')
        reiniciar_app()
    elif idade >= 13 and idade <= 18:
        print(f'\n{nome} você tem {idade} anos, logo você é Adolescente')
        reiniciar_app()
    elif idade >= 19:
        print(f'\n{nome} você tem {idade} anos, logo você é Adulto')
        reiniciar_app()
    else:
        print(f'\nResposta inválida')
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