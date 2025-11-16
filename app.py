import tkinter as tk
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
    nome = entry_nome.get()
    preco = float(entry_preco.get())
    quantidade = int(entry_quantidade.get())
    controller.adicionar(nome, preco, quantidade)
    atualizar_lista()

def deletar():
    item = lista.get(tk.ACTIVE)
    if item:
        id = int(item.split(" - ")[0])
        controller.deletar(id)
        atualizar_lista()

root = tk.Tk()
root.title("Cadastro de Produtos")

tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Preço:").pack()
entry_preco = tk.Entry(root)
entry_preco.pack()

tk.Label(root, text="Quantidade:").pack()
entry_quantidade = tk.Entry(root)
entry_quantidade.pack()

tk.Button(root, text="Adicionar", command=adicionar).pack(pady=5)

lista = tk.Listbox(root, width=50)
lista.pack()

tk.Button(root, text="Deletar Selecionado", command=deletar).pack(pady=5)

atualizar_lista()

root.mainloop()
