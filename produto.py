class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome      # Nome do produto
        self.preco = preco    # Preço do produto
        self.estoque = estoque  # Quantidade em estoque

    def exibir_detalhes(self):
         print(f"Produto: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades")

    def  preco_final(self):
        print(f"Preço final do produto {self.nome}: R${self.preco}")

    def emitir_nota(self):
        print("Nota gerada para PRODUTO.") 

    def repor(self, quantidade):
        self.estoque += quantidade
        
    def vender(self, quantidade):
        self.estoque -= quantidade