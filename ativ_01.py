import os

def nome():
    print('Olá seja bem vindo a atividade 01, qual é o seu nome?')
    user = input()

    print(f'\n {user} digite R para continuar ou qualquer tecla para finalizar.')
    reiniciar = input()
    escolha = reiniciar.upper()

    if escolha == 'R':
        atividade01()
    else:
        finalizar_app()

def reiniciar_app():

    print(f'\nDigite R para continuar ou qualquer tecla para finalizar.')
    reiniciar = input()
    escolha = reiniciar.upper()

    if escolha == 'R':
        atividade01()
    else:
        finalizar_app()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')

def atividade01():
    pergunta = int(input('\nMe diga um número para saber se é par ou impar: '))

    if pergunta %2 == 0 and pergunta > 0:
        print(f'\nO valor escolhido {pergunta} é par')
        reiniciar_app()
    elif pergunta == 0:
        print(f'\nO valor escolhido {pergunta} é neutro')
        reiniciar_app()
    else: 
        print(f'\nO valor escolhido {pergunta} é impar')
        reiniciar_app()

def main():
    os.system('cls')
    nome()

if __name__ == '__main__':
    main()