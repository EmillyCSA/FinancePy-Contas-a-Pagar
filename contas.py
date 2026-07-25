
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

#Listar contas

def listar_contas():
    cursor.execute("SELECT * FROM contas")

    contas = cursor.fetchall()

    for conta in contas:
        id_conta, nome, valor, vencimento, paga = conta

        print("\n" + "=" * 35)
        print("DETALHES DA CONTA".center(35))
        print("=" * 35)
        print(f"ID..........: {id_conta}")
        print(f"Conta.......: {nome}")
        print(f"Valor.......: R$ {valor:.2f}")
        print(f"Vencimento..: {vencimento}")
        print(f"Status......: {paga}")
        print("=" * 35)
        print(          )
