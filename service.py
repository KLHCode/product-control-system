from repository import ProdutoRepository

class ProdutoService:

    def __init__(self):
        self.repo = ProdutoRepository()

    def criar_produto(self, nome, preco, quantidade):
        if nome == "" or preco <= 0 or quantidade < 0:
            raise ValueError("Dados inválidos!")
        self.repo.criar(nome, preco, quantidade)

    def listar_produtos(self):
        return self.repo.listar()

    def atualizar_produto(self, id, nome, preco, quantidade):
        self.repo.atualizar(id, nome, preco, quantidade)

    def deletar_produto(self, id):
        self.repo.deletar(id)
