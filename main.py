import tkinter as tk
import time
from db import criar_conta, checar_conta_existente, puxar_dados


root = tk.Tk()
root.title("Sistema de Banco")
root.geometry("400x300")


pagina_login = tk.Frame(root)
pagina_login.pack()


usuario_text = tk.Label(pagina_login, text="Login:")
usuario_text.pack()

entrada_usuario = tk.Entry(pagina_login,)
entrada_usuario.pack()

senha_text = tk.Label(pagina_login, text="CPF:")
senha_text.pack()

entrada_senha = tk.Entry(pagina_login)
entrada_senha.pack()

def login():
    titular = entrada_usuario.get().strip() # Sempre use strip
    cpf = entrada_senha.get().strip()

    if puxar_dados(titular,cpf):
        pagina_login.pack_forget()
        pagina_sistema.pack()


def registro():

    pagina_login.pack_forget()
    pagina_registro = tk.Frame()
    pagina_registro.pack()

    tk.Label(pagina_registro, text="Criação de Conta!").pack()

    titular_text = tk.Label(pagina_registro, text="Nome do Titular:")
    titular_text.pack()

    entrada_titular = tk.Entry(pagina_registro)
    entrada_titular.pack()

    cpf_text = tk.Label(pagina_registro, text="CPF:")
    cpf_text.pack()

    cpf_text = tk.Entry(pagina_registro)
    cpf_text.pack()

    mensagem = tk.Label(pagina_registro)
    mensagem.pack()

    def checar():

        titular = entrada_titular.get().strip()
        cpf = cpf_text.get().strip()

        if not titular or not cpf:
            print("Invalido")
            mensagem['text'] = "Insira algo valido ne porra"
            return
        elif not cpf.isdigit():
            print("Cpf Invalido")
            mensagem['text'] = "Insira um CPF Valido "
            return
        elif checar_conta_existente(cpf):
            print("Ja existe CPF")
            mensagem['text'] = "Conta Já Existente!"
        else:
            criar_conta(titular,cpf)
            print("Conta Criada")
            mensagem['text'] = "Conta Criada."
            time.sleep(1)
            pagina_registro.pack_forget()
            pagina_login.pack()

    tk.Button(pagina_registro,text="Criar Conta",command=checar).pack(pady=20)


entrar_botao = tk.Button(pagina_login,text="Entrar",command=login)
entrar_botao.pack(pady=20)

criar_conta_botao = tk.Button(pagina_login,text="Registrar",command=registro)
criar_conta_botao.pack(pady=20)




mensagem_login = tk.Label(pagina_login)
mensagem_login.pack()



pagina_sistema = tk.Frame()

tk.Label(pagina_sistema, text="Bem Vindo!").pack()
tk.Label(pagina_sistema, text=f"0")



























root.mainloop()