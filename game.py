# Importa a classe Calcular do módulo calcular
from models.calcular import Calcular


# Define a função main que não recebe argumentos e não retorna nada
def main() -> None:
    # Define a variável pontos como zero
    pontos: int = 0
    # Chama a função jogar passando a variável pontos como argumento
    jogar(pontos)


# Define a função jogar que recebe um argumento pontos do tipo inteiro e não retorna nada
def jogar(pontos: int) -> None:
    # Pede ao usuário para informar a dificuldade desejada e armazena na variável dificuldade como inteiro
    dificuldade: int = int(input('Informe a dificuldade desejada [1, 2, 3 ou 4]: '))

    # Cria um objeto da classe Calcular passando a dificuldade como argumento e armazena na variável calc
    calc: Calcular = Calcular(dificuldade)

    # Imprime na tela a mensagem "Informe o resultado para a seguinte operação"
    print('Informe o resultado para a seguinte operação')
    # Chama a função mostrar_operacao do objeto calc
    calc.mostrar_operacao()

    # Pede ao usuário para informar o resultado da operação e armazena na variável resultado como inteiro
    resultado: int = int(input())

    # Verifica se o resultado informado é correto usando a função checar_resultado do objeto calc
    if calc.checar_resultado(resultado):
        # Se o resultado for correto, incrementa a variável "pontos" em 1 e imprime na tela a mensagem com a pontuação
        # atual
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    # Pede ao usuário para informar se deseja continuar no jogo e armazena na variável continuar como inteiro
    continuar: int = int(input('Deseja continuar no jogo? [1 - Sim, 0 - Não]'))

    # Se o usuário deseja continuar, chama a função jogar novamente passando a variável pontos como argumento
    if continuar:
        jogar(pontos)
    # Se o usuário não deseja continuar, imprime na tela a mensagem com a pontuação final e encerra o jogo
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Obrigado e até a próxima!')


# Verifica se o módulo está sendo executado diretamente e chama a função main se for o caso
if __name__ == '__main__':
    main()
