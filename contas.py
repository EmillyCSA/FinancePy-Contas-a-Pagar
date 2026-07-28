
from banco import conexao, cursor

def cadastrar_conta ():
    print("\n" + "=" * 35)
    print("CADASTRO DE CONTA".center(35))
    print("=" * 35)

    nome_conta = input ("Nome da conta: ")
    valor = input ("Valor da conta: ")    
    vencimento = input ("Vencimento: ")
    cursor.execute("""
    INSERT INTO contas (nome, valor, vencimento, paga)
    VALUES (?, ?, ?, ?)
    """, (nome_conta, valor, vencimento, "Não"))

    conexao.commit()

    print ("✅ Conta cadastrada com sucesso!")
    print ()

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
        print()

#Criar e definir a função 3: Marcar conta como paga

def marcar_conta_paga():
    print("\n" + "=" * 35)
    print("MARCAR CONTA COMO PAGA".center(35))
    print("=" * 35)

    id_conta = input("Digite o ID da conta: ")

    cursor.execute("""
    UPDATE contas
    SET paga = ?
    WHERE id = ?
    """, ("Sim", id_conta))

    if cursor.rowcount == 0:
        print()
        print("❌ Conta não encontrada!")
        print()
    else:
        conexao.commit()

        print()
        print("✅ Conta marcada como paga com sucesso!")
        print()

# Função:4 Excluir conta

def excluir_conta():
    print ("\n" + "=" * 35)
    print ("EXCLUIR CONTA" .center(35))
    print("=" * 35)

    id_conta = input ("Digite o ID da conta: ")

    cursor.execute("""
    DELETE FROM contas
    WHERE id = ? ;
    """ , (id_conta,))

    if cursor.rowcount == 0:
        print()
        print("❌ Conta não encontrada!")
        print()
    else:
        conexao.commit()
        print ()
        print ("✅ Conta excluída com sucesso !")
        print ()


# Função :5  Resumo Financeiro

def resumo_financeiro():
    print ("\n" + "=" * 35)
    print ("RESUMO FINANCEIRO" .center(35))
    print ("=" * 35)

    cursor.execute("""
    SELECT COUNT(*)
    FROM contas
    """)

    total_contas = cursor.fetchone()[0]

    print()
    print(f"📋 Total de contas: {total_contas}")
    print()

    cursor.execute("""
    SELECT SUM(valor)
    FROM contas
    """)

    valor_total = cursor.fetchone()[0]

    print(f"💰 Valor total: R$ {valor_total:.2f}")
    print()

    cursor.execute("""
    SELECT COUNT(*)
    FROM contas
    WHERE paga = ?
    """, ("Sim",))

    contas_pagas = cursor.fetchone()[0]

    print(f"✅ Contas pagas: {contas_pagas}")
    print ()

    cursor.execute("""
    SELECT COUNT(*)
    FROM contas
    WHERE paga = ?
    """, ("Não",))

    contas_pendentes = cursor.fetchone()[0]

    print(f"🕒 Contas pendentes: {contas_pendentes}")
    print()

    cursor.execute("""
    SELECT SUM(valor)
    FROM contas
    WHERE paga = ?
    """, ("Não",))

    valor_pendente = cursor.fetchone()[0]

    print(f"💸 Valor pendente: R$ {valor_pendente:.2f}")
    print()

# Função:6 - Editor de Contas

def editar_conta():
    print("\n" + "=" * 35)
    print("EDITAR CONTA".center(35))
    print("=" * 35)

    id_conta = input("Digite o ID da conta: ")
    print()

    cursor.execute("""
    SELECT *
    FROM contas
    WHERE id = ?
    """, (id_conta,))

    conta = cursor.fetchone()

    if conta is None:
        print()
        print("❌ Conta não encontrada!")
        print()
        return

    id_conta, nome, valor, vencimento, paga = conta

    print()
    print(f"Conta atual.......: {nome}")
    print(f"Valor atual.......: R$ {valor:.2f}")
    print(f"Vencimento atual..: {vencimento}")
    print()

    novo_nome = input("Novo nome da conta: ")
    novo_valor = input("Novo valor: ")
    novo_vencimento = input("Novo vencimento: ")
    print()

    cursor.execute("""
    UPDATE contas
    SET nome = ?, valor = ?, vencimento = ?
    WHERE id = ?
    """, (novo_nome, novo_valor, novo_vencimento, id_conta))

    conexao.commit()

    print()
    print("✅ Conta atualizada com sucesso!")
    print()