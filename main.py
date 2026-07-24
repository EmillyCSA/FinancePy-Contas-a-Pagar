#Início de projeto - Menu Principal

# Importa a função responsável por exibir o menu principal
import banco
from menu import menu_principal
from contas import cadastrar_conta

while True:
    menu_principal()

# Solicita que o usuário escolha uma opção
    opcao = input ("Escolha uma opção: ")

# Verifica a opção escolhida
    if opcao == "1":
        cadastrar_conta ()
    elif opcao == "2":
        print ("Listar contas: ")
    elif opcao == "3":
        print ( "Marcar conta como paga: ")
    elif opcao == "4":
        print ( "Excluir conta: ")
    elif opcao == "5":
        print ( "Resumo Financeiro: ")
    elif opcao == "0":
        print ("Sair/Finazlizado")
        break

else:
    print ("Opção Inválida")



