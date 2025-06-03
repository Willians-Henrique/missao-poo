from funcionario_pj import FuncionarioPJ
from funcionario_clt import FuncionarioCLT

funcionario1 = FuncionarioPJ("will", 190, 22)
funcionario2 = FuncionarioCLT('Maria', 2000)

print(f"pagamento de {funcionario1.nome}: R${funcionario1.calcular_pagamento()}")
print(f"pagamento de {funcionario2.nome}: R${funcionario2.calcular_pagamento()}")

