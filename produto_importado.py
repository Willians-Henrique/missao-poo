from produto import Produto

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_importacao = taxa_importacao

    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades| Taxa de importação: {self.taxa_importacao}")    