class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, codigo, nome, preco, quantidade):
        produto = Produto(codigo, nome, preco, quantidade)
        self.produtos.append(produto)

    def remover_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                return True
        return False

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}")

estoque = Estoque()

# Adicionando um produto
estoque.adicionar_produto(1, "Camiseta", 50.0, 100)

# Removendo um produto
estoque.remover_produto(1)

# Listando todos os produtos
estoque.listar_produtos()
