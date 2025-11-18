import tkinter as tk  # Biblioteca para criar interface gráfica
from tkinter import messagebox  # Para mostrar alertas e erros na GUI
from controller import ProdutoController  # Controller para gerenciar CRUD dos produtos
from database import init_db  # Função para inicializar o banco de dados

# Inicializa o controller e o banco de dados
controller = ProdutoController()
init_db()

# -------------------------
# Funções da interface
# -------------------------

# Atualiza a lista de produtos exibida na Listbox
def atualizar_lista():
    lista.delete(0, tk.END)  # Limpa todos os itens da lista
    produtos = controller.listar()  # Busca todos os produtos no banco
    for p in produtos:
        # Insere cada produto na lista, no formato: ID - Nome | Preço | Quantidade
        lista.insert(tk.END, f"{p[0]} - {p[1]} | R$ {p[2]} | Qtd: {p[3]}")

# Adiciona um novo produto
def adicionar():
    try:
        # Pega os valores digitados nos campos
        nome = entry_nome.get()
        preco = float(entry_preco.get())  # Converte para float
        quantidade = int(entry_quantidade.get())  # Converte para int

        # Chama a função do controller para adicionar o produto
        controller.adicionar(nome, preco, quantidade)

        # Atualiza a lista de produtos na interface
        atualizar_lista()

        # Limpa os campos de entrada após adicionar
        entry_nome.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
    except:
        # Mostra um erro caso os dados inseridos sejam inválidos
        messagebox.showerror("Erro", "Verifique os dados inseridos.")

# Deleta o produto selecionado
def deletar():
    item = lista.get(tk.ACTIVE)  # Pega o item selecionado
    if not item:
        messagebox.showwarning("Aviso", "Selecione um produto para deletar.")
        return

    # Extrai o ID do produto da string
    id = int(item.split(" - ")[0])
    controller.deletar(id)  # Chama a função do controller para deletar
    atualizar_lista()  # Atualiza a lista na interface

# Abre uma janela para atualizar o produto selecionado
def abrir_janela_atualizar():
    item = lista.get(tk.ACTIVE)  # Pega o item selecionado
    if not item:
        messagebox.showwarning("Aviso", "Selecione um produto para atualizar.")
        return

    # Extrai os dados do produto
    id, resto = item.split(" - ")
    nome, resto = resto.split(" | R$ ")
    preco, qtd_texto = resto.split(" | Qtd: ")
    quantidade = qtd_texto

    # Cria uma nova janela
    janela = tk.Toplevel(root)
    janela.title("Atualizar Produto")
    janela.geometry("250x200")

    # Campo para nome
    tk.Label(janela, text="Nome:").pack()
    entry_nome_up = tk.Entry(janela)
    entry_nome_up.pack()
    entry_nome_up.insert(0, nome)  # Preenche com o nome atual

    # Campo para preço
    tk.Label(janela, text="Preço:").pack()
    entry_preco_up = tk.Entry(janela)
    entry_preco_up.pack()
    entry_preco_up.insert(0, preco)  # Preenche com o preço atual

    # Campo para quantidade
    tk.Label(janela, text="Quantidade:").pack()
    entry_qtd_up = tk.Entry(janela)
    entry_qtd_up.pack()
    entry_qtd_up.insert(0, quantidade)  # Preenche com a quantidade atual

    # Função para salvar a atualização
    def salvar_atualizacao():
        try:
            novo_nome = entry_nome_up.get()
            novo_preco = float(entry_preco_up.get())
            nova_qtd = int(entry_qtd_up.get())

            controller.atualizar(int(id), novo_nome, novo_preco, nova_qtd)  # Atualiza no banco
            atualizar_lista()  # Atualiza a lista na interface
            janela.destroy()  # Fecha a janela
        except:
            messagebox.showerror("Erro", "Dados inválidos.")

    # Botão para salvar alterações
    tk.Button(janela, text="Salvar", command=salvar_atualizacao).pack(pady=10)

# -------------------------
# Interface Principal
# -------------------------

root = tk.Tk()  # Cria a janela principal
root.title("Cadastro de Produtos")
root.geometry("350x450")

# Campo de entrada para nome
tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

# Campo de entrada para preço
tk.Label(root, text="Preço:").pack()
entry_preco = tk.Entry(root)
entry_preco.pack()

# Campo de entrada para quantidade
tk.Label(root, text="Quantidade:").pack()
entry_quantidade = tk.Entry(root)
entry_quantidade.pack()

# Botão para adicionar produto
tk.Button(root, text="Adicionar", width=20, command=adicionar).pack(pady=5)

# Lista de produtos
lista = tk.Listbox(root, width=50)
lista.pack()

# Botões para atualizar e deletar
tk.Button(root, text="Atualizar Selecionado", width=20, command=abrir_janela_atualizar).pack(pady=5)
tk.Button(root, text="Deletar Selecionado", width=20, command=deletar).pack(pady=5)

# Atualiza a lista assim que a interface abre
atualizar_lista()

# Mantém a janela aberta
root.mainloop()
