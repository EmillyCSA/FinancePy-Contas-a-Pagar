import sqlite3

conexao = sqlite3.connect("financepy.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    valor REAL NOT NULL,
    vencimento TEXT NOT NULL,
    paga TEXT NOT NULL
)
""")

conexao.commit()

