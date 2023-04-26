# Importa a classe Calcular do módulo models.calcular
from models.calcular import Calcular

# Instancia um objeto da classe Calcular com dificuldade 1
calc: Calcular = Calcular(1)

# Imprime o valor retornado pelo método __str__ da classe Calcular
print(calc)
