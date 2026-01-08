import sqlite3

connection = sqlite3.connect("banco.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               titular TEXT NOT NULL, 
               saldo FLOAT NOT NULL,
               cpf TEXT NOT NULL UNIQUE,
               senha TEXT NOT NULL 
               )""")

def checar_conta_existente(cpf):
    cursor.execute("SELECT cpf FROM contas_bancarias")
    cpf_puxado = cursor.fetchall()
    if cpf in cpf_puxado:
        return True
    else:
        return False


def criar_conta(titular,cpf,senha):
    # 1. Usamos '?' como lugar reservado. O banco se vira com aspas e tipos.
    # 2. Adicionamos a palavra VALUES.
    sql = "INSERT INTO contas_bancarias (titular, saldo, cpf, senha) VALUES (?, 0, ?, ?)"
    
    # 3. Passamos as variáveis numa tupla separada
    cursor.execute(sql, (titular, cpf, senha))
    
    # 4. OBRIGATÓRIO: Salvar as alterações no arquivo
    # Nota: O commit é feito na CONEXÃO, não no cursor.
    # Se sua variável de conexão se chama 'conexao' ou 'conn', use ela aqui.
    connection.commit()

def puxar_dados(cpf, senha):
    # O SQL só retorna algo se o nome E o cpf baterem
    cursor.execute("SELECT * FROM contas_bancarias WHERE cpf = ? AND senha = ?", (cpf, senha))
    resultado = cursor.fetchone() # Pega apenas o primeiro resultado (ou None)
    
    # Se resultado não for None (vazio), o usuário existe
    return resultado is not None

def pegar_info(cpf):
    cursor.execute("SELECT * FROM contas_bancarias WHERE cpf = ?", (cpf))
    resultado = cursor.fetchall()

    return resultado

def saque(valor):
    cursor.execute("SELECT saldo FROM contas_bancarias")
    resultado = cursor.fetchone()
    saldo = resultado[0]

    if valor < saldo:
        print("Saldo Insuficiente")
    else:
        print("Saldo suficiente")

def depositar(valor, cpf):
    cursor.execute("UPDATE contas_bancarias SET saldo = saldo + ? WHERE cpf = ?", (valor, cpf))
    connection.commit()
    print("Depositado")


connection.commit() 