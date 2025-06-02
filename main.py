from produto import Produto
from produto_nacional import ProdutoNacional
from produto_importado import ProdutoImportado

produto1 = Produto("Teclado1", 100.0, 20)
produto2 = ProdutoNacional("Teclado2", 100.0, 20)
produto3 = ProdutoImportado("Celular", 2000.0, 5, 0.15)
produto1.preco_final()
produto2.preco_final()
produto3.preco_final()

