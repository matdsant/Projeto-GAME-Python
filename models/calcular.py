# Importa a função randint do módulo random
from random import randint


# Define a classe Calcular
class Calcular:

    # Inicializa a classe com os atributos dificuldade, valor1, valor2, operação e resultado
    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade  # Atribui a dificuldade
        self.__valor1: int = self._gerar_valor  # Atribui o valor1 usando o método _gerar_valor
        self.__valor2: int = self._gerar_valor  # Atribui o valor2 usando o método _gerar_valor
        self.__operacao: int = randint(1, 3)  # Atribui a operação com um número aleatório entre 1 e 3
        self.__resultado: int = self._gerar_resultado  # Atribui o resultado usando o método _gerar_resultado

    # Define a propriedade dificuldade
    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    # Define a propriedade valor1
    @property
    def valor1(self: object) -> int:
        return self.__valor1

    # Define a propriedade valor2
    @property
    def valor2(self: object) -> int:
        return self.__valor2

    # Define a propriedade operacao
    @property
    def operacao(self: object) -> int:
        return self.__operacao

    # Define a propriedade resultado
    @property
    def resultado(self: object) -> int:
        return self.__resultado

    # Define o método __str__ que retorna uma string com os valores de valor1, valor2, dificuldade e operação
    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Subtrair'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    # Define o método _gerar_valor que retorna um valor aleatório conforme a dificuldade
    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    # Define o método _gerar_resultado que retorna o resultado da operação
    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:  # Somar
            return self.valor1 + self.valor2
        elif self.operacao == 2:  # Subtrair
            return self.valor1 - self.valor2
        else:  # Multiplicar
            return self.valor1 * self.valor2

    # Define a propriedade _op_simbolo que retorna o símbolo da operação
    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    # Define o método checar_resultado que verifica se a resposta está correta e retorna um booleano
    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    # Define o método mostrar_operacao que mostra a operação a ser realizada
    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
