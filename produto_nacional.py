from produto import Produto

class ProdutoNacional(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)
    
    def emitir_nota(self):
        print("Nota fiscal nacional para PRODUTO.")     
