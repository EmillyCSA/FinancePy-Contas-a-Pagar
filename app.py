from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/")
def inicio():

    # Conecta ao banco de dados
    conexao = sqlite3.connect("financepy.db")
    cursor = conexao.cursor()

    # Conta quantas contas existem
    cursor.execute("SELECT COUNT(*) FROM contas")
    total_contas = cursor.fetchone()[0]

    # Soma o valor de todas as contas
    cursor.execute("SELECT COALESCE(SUM(valor), 0) FROM contas")
    valor_total = cursor.fetchone()[0]

    # Conta quantas contas estão pagas
    cursor.execute("""
        SELECT COUNT(*)
        FROM contas
        WHERE paga = ?
    """, ("Sim",))

    contas_pagas = cursor.fetchone()[0]

    # Conta quantas contas estão pendentes
    cursor.execute("""
        SELECT COUNT(*)
        FROM contas
        WHERE paga = ?
    """, ("Não",))

    contas_pendentes = cursor.fetchone()[0]

    # Fecha a conexão com o banco
    conexao.close()

    # Envia os dados para a página HTML
    return render_template(
        "index.html",
        total_contas=total_contas,
        valor_total=valor_total,
        contas_pagas=contas_pagas,
        contas_pendentes=contas_pendentes
    )


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():

    if request.method == "POST":

        nome = request.form["nome"]
        valor = request.form["valor"]
        vencimento = request.form["vencimento"]

        # Verifica se o nome foi preenchido
        if not nome.strip():
            return render_template(
                "cadastrar.html",
                erro="O nome da conta é obrigatório."
            )

        # Converte o valor para número
        try:
            valor = float(valor)
        except ValueError:
            return render_template(
                "cadastrar.html",
                erro="Digite um valor válido."
            )

        # Verifica se o valor é maior que zero
        if valor <= 0:
            return render_template(
                "cadastrar.html",
                erro="O valor da conta deve ser maior que zero."
            )

        # Verifica se o vencimento foi preenchido
        if not vencimento:
            return render_template(
                "cadastrar.html",
                erro="A data de vencimento é obrigatória."
            )

        # Conecta ao banco de dados
        conexao = sqlite3.connect("financepy.db")
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO contas (nome, valor, vencimento, paga)
            VALUES (?, ?, ?, ?)
        """, (nome, valor, vencimento, "Não"))

        conexao.commit()
        conexao.close()

        return redirect("/")

    return render_template("cadastrar.html")


@app.route("/listar")
def listar():

    # Conecta ao banco de dados
    conexao = sqlite3.connect("financepy.db")
    cursor = conexao.cursor()

    # Busca todas as contas cadastradas
    cursor.execute("""
        SELECT id, nome, valor, vencimento, paga
        FROM contas
        ORDER BY id
    """)

    contas = cursor.fetchall()

    # Fecha a conexão
    conexao.close()

    # Envia as contas para o HTML
    return render_template("listar.html", contas=contas)


@app.route("/resumo")
def resumo():

    # Conecta ao banco de dados
    conexao = sqlite3.connect("financepy.db")
    cursor = conexao.cursor()

    # Conta o total de contas
    cursor.execute("""
        SELECT COUNT(*)
        FROM contas
    """)

    total_contas = cursor.fetchone()[0]

    # Soma o valor de todas as contas
    cursor.execute("""
        SELECT COALESCE(SUM(valor), 0)
        FROM contas
    """)

    valor_total = cursor.fetchone()[0]

    # Conta quantas contas estão pagas
    cursor.execute("""
        SELECT COUNT(*)
        FROM contas
        WHERE paga = ?
    """, ("Sim",))

    contas_pagas = cursor.fetchone()[0]

    # Conta quantas contas estão pendentes
    cursor.execute("""
        SELECT COUNT(*)
        FROM contas
        WHERE paga = ?
    """, ("Não",))

    contas_pendentes = cursor.fetchone()[0]

    # Soma o valor das contas pendentes
    cursor.execute("""
        SELECT COALESCE(SUM(valor), 0)
        FROM contas
        WHERE paga = ?
    """, ("Não",))

    valor_pendente = cursor.fetchone()[0]

    # Fecha a conexão com o banco
    conexao.close()

    # Envia os dados para a página de resumo
    return render_template(
        "resumo.html",
        total_contas=total_contas,
        valor_total=valor_total,
        contas_pagas=contas_pagas,
        contas_pendentes=contas_pendentes,
        valor_pendente=valor_pendente
    )


if __name__ == "__main__":
    app.run(debug=True)

