class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome      # Nome do produto
        self.preco = preco    # Preço do produto
        self.estoque = estoque  # Quantidade em estoque

    def exibir_detalhes(self):
         print(f"Produto: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades")