import tkinter as tk
import time
from db import pegar_info, saque, depositar


def conversor(texto):
    texto_limpo = texto.replace(",", ".")


    try:
        return float(texto_limpo)
    except ValueError:
        print("Erro, não é um numero valido")
        return None



def pagina_sistema():


    def pagina_sacar():

        def saque_verificacao():
            valor_saque = entrada_saque.get().strip()
            valor_correto = conversor(valor_saque)

            saque(valor_correto)

        pagina_saque = tk.Frame()

        pagina_sistema.pack_forget()
        pagina_saque.pack()

        tk.Label(pagina_saque,text="Sacar").pack()
        tk.Label(pagina_saque, text="Quanto deseja sacar?").pack(pady=25)

        entrada_saque = tk.Entry(pagina_saque)
        entrada_saque.pack()

        tk.Button(text="Sacar",command=saque_verificacao).pack()


    def pagina_depositar():

        for info in pegar_info():
            id, titular, saldo, cpf, senha = info

        def deposito():
            valor = entrada_deposito.get().strip()
            valor_correto = conversor(valor)

            depositar(valor_correto,cpf)

        pagina_deposito = tk.Frame()

        pagina_sistema.pack_forget()
        pagina_deposito.pack()

        tk.Label(pagina_deposito,text="Depositar").pack()
        tk.Label(pagina_deposito, text="Quanto deseja Depositar?").pack(pady=25)

        entrada_deposito = tk.Entry(pagina_deposito)
        entrada_deposito.pack()

        tk.Button(text="Depositar",command=deposito).pack()
            


    for info in pegar_info():
        id, titular, saldo, cpf, senha = info
    
    print(info)

    pagina_sistema = tk.Frame()
    
    tk.Label(pagina_sistema, text=f"Bem Vindo! {titular}.").pack()
    tk.Label(pagina_sistema, text=f"R${saldo:.2f}").pack(pady=20)

    tk.Button(pagina_sistema,text="Depositar",command=pagina_depositar).pack(pady=5)
    tk.Button(pagina_sistema,text="Sacar",command=pagina_sacar).pack(pady=5)
    tk.Button(pagina_sistema,text="Transferir",command=transferir).pack(pady=5)

    pagina_sistema.pack()





def transferir():
    ...
