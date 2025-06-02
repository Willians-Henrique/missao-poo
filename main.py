from produto_nacional import ProdutoNacional
from produto_importado import ProdutoImportado

produto1 = ProdutoNacional("Teclado", 100.0, 20)
produto1.exibir_detalhes()
produto2 = ProdutoImportado("Celular", 2000.0, 5, 0.15)
produto2.exibir_detalhes()

