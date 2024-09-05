# Programa para fazer depósitos, saques e imprimir extratos:

def main():
    # Constantes:
    NUMERO_MAXIMO_DE_SAQUES = 3
    VALOR_LIMITE_POR_SAQUE = 500

    #  Variáveis:
    saldo = 0
    extrato = "\n"
    numero_de_saques = 0

    while True:
        opcao = leitura()

        if opcao.lower() == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao.lower() == "s":
            saldo, extrato, numero_de_saques = sacar(saldo, extrato, numero_de_saques, NUMERO_MAXIMO_DE_SAQUES, VALOR_LIMITE_POR_SAQUE)
        elif opcao.lower() == "e":
            print(extrato)
            print(f"--------------------\nsaldo:    R$ {saldo:.2f}\n")
        elif opcao.lower() == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Define o Menu principal e retorna o valor da opção escolhida:
def leitura():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """
    opcao = input(menu)
    return opcao

# função que realiza do depósito:
def depositar(saldo, extrato):
    # Realiza a leitura do valor a ser depositado:
    valor_a_depositar = input("Por favor, informe o valor a ser depositado: ")

    # Analisa se o valor é um número positivo. Se negativo, retorna -1:
    valor_a_depositar = eh_numero_positivo(valor_a_depositar)

    # Se o valor_a_depositar é válido, realiza o depósito.
    if valor_a_depositar != -1:
        saldo += valor_a_depositar
        extrato += f"Depósito: R$ {valor_a_depositar:.2f}\n"
        print("Depósito realizado com sucesso.")
    # Se o valor_a_depositar não é válido, informa o erro:
    else:
        print("\nErro: o valor informado não é válido.")

    # Retorna o saldo e extrato:
    return saldo, extrato

# Função que realiza o saque:
def sacar(saldo, extrato, numero_de_saques, NUMERO_MAXIMO_DE_SAQUES, VALOR_LIMITE_POR_SAQUE):
    # Realiza a leitura do valor a ser sacado:
    valor_a_sacar = input("Por favor, informe o valor a ser sacado: ")

    # Analisa se o valor é um número positivo. Se negativo, retorna -1:
    valor_a_sacar = eh_numero_positivo(valor_a_sacar)

    # Se o valor_a_sacar não é válido, informa o erro:
    if valor_a_sacar == -1:
        print("\nErro: o valor informado não é válido.")
        
    # Se o valor_a_sacar é superior ao saldo, informa o erro:
    elif valor_a_sacar > saldo:
        print("\nErro: saldo insuficiente.")
        
    # Se o valor_a_sacar é superior ao valor limite por saque, informa o erro:
    elif valor_a_sacar > VALOR_LIMITE_POR_SAQUE:
        print(f"\nErro: valor superior ao limite por saque: R$ {VALOR_LIMITE_POR_SAQUE:.2f}.")

    # Se o numero_de_saques é superior ao numero máximo de saques, informa o erro:
    elif numero_de_saques >= NUMERO_MAXIMO_DE_SAQUES:
        print(f"\nErro: número de saques superior ao limite diário: {NUMERO_MAXIMO_DE_SAQUES} saques.")
    # Todas condições satisfeitas, realiza-se o saque:
    else:
        saldo -= valor_a_sacar
        extrato += f"Saque:    R$ {valor_a_sacar:.2f}\n"
        numero_de_saques += 1
        print("Saque realizado com sucesso.")

    # Retorna o saldo e extrato atualizado:
    return saldo, extrato, numero_de_saques

# Função que verifica se a string é um número positivo, caso negativo, retorna -1:
def eh_numero_positivo(s):
    try:
        numero = float(s)
        if numero >= 0:
            return numero
    except ValueError:
        return -1
    return -1

main()

