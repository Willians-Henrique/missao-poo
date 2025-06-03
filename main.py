from produto import Produto
from produto_nacional import ProdutoNacional
from produto_importado import ProdutoImportado

produto1 = Produto("Teclado1", 100.0, 20)
produto2 = ProdutoNacional("Teclado2", 100.0, 20)
produto3 = ProdutoImportado("Celular", 2000.0, 5, 0.15)

produto1.repor(10)
print(f"Estoque do produto {produto1.nome} atualizado para {produto1.estoque} unidades.")

produto1.vender(20)
print(f"Estoque do produto {produto1.nome} atualizado para {produto1.estoque} unidades.")


