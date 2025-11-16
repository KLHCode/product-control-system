from database import get_connection

class ProdutoRepository:

    def criar(self, nome, preco, quantidade):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
                       (nome, preco, quantidade))
        conn.commit()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        dados = cursor.fetchall()
        conn.close()
        return dados

    def atualizar(self, id, nome, preco, quantidade):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE produtos SET nome=?, preco=?, quantidade=? WHERE id=?",
                       (nome, preco, quantidade, id))
        conn.commit()
        conn.close()

    def deletar(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id=?", (id,))
        conn.commit()
        conn.close()
