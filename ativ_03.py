import os

def ativ02():
    print('\nOlá seja bem vindo a atividade 03, crie um log de usuário:')
    log_01 = input()

    print('\nAgora me informe uma senha:')
    senha_01 = input()

    print('\nAgora vamos confirmar os seus dados, me diga novamente qual o seu log')
    log_02 = input()

    print('\nAgora me informe a sua senha:')
    senha_02 = input()

    if log_01 == log_02 and senha_01 == senha_02:
        print(f'\nAcesso aceito!')
        reiniciar_app()
    else:
        print(f'\nAcesso Negado!')

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