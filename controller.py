from service import ProdutoService

class ProdutoController:

    def __init__(self):
        self.service = ProdutoService()

    def adicionar(self, nome, preco, quantidade):
        self.service.criar_produto(nome, preco, quantidade)

    def listar(self):
        return self.service.listar_produtos()

    def atualizar(self, id, nome, preco, quantidade):
        self.service.atualizar_produto(id, nome, preco, quantidade)

    def deletar(self, id):
        self.service.deletar(id)
