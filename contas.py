
from banco import conexao, cursor

def cadastrar_conta ():
    print (    "Cadastro de conta ")

    nome_conta = input ("Nome da conta: ")
    valor = input ("Valor da conta: ")    
    vencimento = input ("Vencimento: ")
    cursor.execute("""
    INSERT INTO contas (nome, valor, vencimento, paga)
    VALUES (?, ?, ?, ?)
    """, (nome_conta, valor, vencimento, "Não"))

    conexao.commit()

    print ("Conta cadastrada com sucesso!")
    print (             )

