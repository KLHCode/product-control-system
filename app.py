import tkinter as tk
from tkinter import messagebox
from controller import ProdutoController
from database import init_db

controller = ProdutoController()
init_db()

def atualizar_lista():
    lista.delete(0, tk.END)
    produtos = controller.listar()
    for p in produtos:
        lista.insert(tk.END, f"{p[0]} - {p[1]} | R$ {p[2]} | Qtd: {p[3]}")

def adicionar():
    try:
        nome = entry_nome.get()
        preco = float(entry_preco.get())
        quantidade = int(entry_quantidade.get())
        controller.adicionar(nome, preco, quantidade)
        atualizar_lista()
        entry_nome.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
    except:
        messagebox.showerror("Erro", "Verifique os dados inseridos.")

def deletar():
    item = lista.get(tk.ACTIVE)
    if not item:
        messagebox.showwarning("Aviso", "Selecione um produto para deletar.")
        return

    id = int(item.split(" - ")[0])
    controller.deletar(id)
    atualizar_lista()

def abrir_janela_atualizar():
    item = lista.get(tk.ACTIVE)
    if not item:
        messagebox.showwarning("Aviso", "Selecione um produto para atualizar.")
        return

    id, resto = item.split(" - ")
    nome, resto = resto.split(" | R$ ")
    preco, qtd_texto = resto.split(" | Qtd: ")
    quantidade = qtd_texto

    janela = tk.Toplevel(root)
    janela.title("Atualizar Produto")
    janela.geometry("250x200")

    tk.Label(janela, text="Nome:").pack()
    entry_nome_up = tk.Entry(janela)
    entry_nome_up.pack()
    entry_nome_up.insert(0, nome)

    tk.Label(janela, text="Preço:").pack()
    entry_preco_up = tk.Entry(janela)
    entry_preco_up.pack()
    entry_preco_up.insert(0, preco)

    tk.Label(janela, text="Quantidade:").pack()
    entry_qtd_up = tk.Entry(janela)
    entry_qtd_up.pack()
    entry_qtd_up.insert(0, quantidade)

    def salvar_atualizacao():
        try:
            novo_nome = entry_nome_up.get()
            novo_preco = float(entry_preco_up.get())
            nova_qtd = int(entry_qtd_up.get())

            controller.atualizar(int(id), novo_nome, novo_preco, nova_qtd)
            atualizar_lista()
            janela.destroy()
        except:
            messagebox.showerror("Erro", "Dados inválidos.")

    tk.Button(janela, text="Salvar", command=salvar_atualizacao).pack(pady=10)

# -------------------------
# Interface Principal
# -------------------------

root = tk.Tk()
root.title("Cadastro de Produtos")
root.geometry("350x450")

tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Preço:").pack()
entry_preco = tk.Entry(root)
entry_preco.pack()

tk.Label(root, text="Quantidade:").pack()
entry_quantidade = tk.Entry(root)
entry_quantidade.pack()

tk.Button(root, text="Adicionar", width=20, command=adicionar).pack(pady=5)

lista = tk.Listbox(root, width=50)
lista.pack()

tk.Button(root, text="Atualizar Selecionado", width=20, command=abrir_janela_atualizar).pack(pady=5)
tk.Button(root, text="Deletar Selecionado", width=20, command=deletar).pack(pady=5)

atualizar_lista()
root.mainloop()
