import sqlite3

conexao = sqlite3.connect("main.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
    nome TEXT NOT NULL,
    preco INTEGER NOT NULL
)""")

conexao.commit()

def admin():
    print()
    print("=== AREA DO ADMIN ===")
    acesso = input("Digite a senha de acesso:")

    if acesso == 2026:
        print()
        print("ACESSO CONCEDIDO!")
        print()
    else:
        print()
        print("ACESSO NEGADO!")
        print()
        return

    print("=== PRODUTOS ===")
    print("1 Ver produtos")
    print("2 Adicionar produtos")

    escolha = int(input("Escolha: "))

    if escolha == 1:
        ver()
    elif escolha == 2:
        add()
    else:
        print()
        print("Opção Invalida!")
        print()
        return

def cliente():
    print()
    print("==== AREA DO CLIENE ====")
    print("1 Ver Produtos")
    print("2 Comprar produtos")

    escolha = int(input("Escolha: "))

    if escolha == 1:
        ver()
    elif escolha == 2:
        buy()
    else:
        print()
        print("Opção invalida!")
        print()

def buy():
    print()
    cursor.execute("""SELECT * FROM produtos""")
    resultado = cursor.fetchall()
    
    for resultados in resultado():
        print(resultados)

    escolha = input("Escolha um produto: ")

    print()
    print("Pedido feito!")
    print("Informações:")
    print(f"Produto: {escolha}")
    print()

def ver():
    cursor.execute("""SELECT * FROM produtos""")
    resultado = cursor.fetchall()

    for resultados in resultado():
        print(resultados)

def add():
    print()
    newname = input("Digite o nome do produto: ")
    newprice = float(input("Digite o preço do produto: "))

    try:
        cursor.execute("""
        INSERT INTO produtos 
        (nome, preco) VALUES 
        (?, ?)""", (newname, newprice))
        print()
        print("Produto adicionado com sucesso!")
        print()

    except:
        print()
        print("Caracteres invalidos...")

while True:
    print("= = AREA DE ACESSO = =")
    print("1 Area do cliente")
    print("2 Area administrativa")

    escolha = int(input("Escolha: "))

    if escolha == 1:
        cliente()
    elif escolha == 2:
        admin()
    else:
        print()
        print("Opção Invalida...")
        print()
