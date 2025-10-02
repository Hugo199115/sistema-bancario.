# -*- coding: utf-8 -*-
"""Sistema Bancário v2.0"""

# Variáveis principais
saldo = 0.0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
movimentacoes = []  # lista para registrar as operações
usuarios = []       # lista de usuários
contas = []         # lista de contas
AGENCIA = "0001"    # agência padrão


def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        movimentacoes.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")


def sacar(valor):
    global saldo, numero_saques
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        movimentacoes.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")


def exibir_extrato():
    print("\n=========== EXTRATO ===========")
    if movimentacoes:
        for mov in movimentacoes:
            print(mov)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=================================")


def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Verifica se já existe usuário com o mesmo CPF
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario:
        print("⚠️ Já existe um usuário com esse CPF!")
        return

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print(f"✅ Usuário {nome} criado com sucesso!")


def criar_conta(cpf):
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if not usuario:
        print("⚠️ Usuário não encontrado. Cadastre primeiro o usuário.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "usuario": usuario
    })
    print(f"✅ Conta {numero_conta} criada com sucesso para {usuario['nome']}!")


def listar_contas():
    for conta in contas:
        usuario = conta["usuario"]["nome"]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {usuario}")


def menu():
    return input("""
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[c] Criar conta
[l] Listar contas
[q] Sair

=> """)


# Loop principal
while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "u":
        nome = input("Nome completo: ")
        data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        cpf = input("CPF (somente números): ")
        endereco = input("Endereço (logradouro, número - bairro - cidade/sigla estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        criar_conta(cpf)

    elif opcao == "l":
        listar_contas()

    elif opcao == "q":
        print("Saindo do sistema... Obrigado!")
        break

    else:
        print("Operação inválida! Selecione novamente.")
