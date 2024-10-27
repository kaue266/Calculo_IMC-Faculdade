"""
Este módulo calcula o IMC e exibe uma tabela de classificação de IMC.
"""

from rich.table import Table
from rich.console import Console

console = Console()

def calcula_imc(peso: float, altura: float) -> float:
    """Calcula o IMC a partir do peso e altura recebidos."""
    imc = peso / (altura * altura)
    imc_arredondado = round(imc, 2)
    return imc_arredondado

def exibir_tabela_imc():
    """Mostra uma tabela com os dados do IMC para o usuário."""
    tabela = Table(title="Tabela de IMC")
    tabela.add_column("IMC", justify="center", style="cyan", no_wrap=True)
    tabela.add_column("Classificação", justify="center", style="white")
    tabela.add_row("Menos de 18.5", "Abaixo do peso")
    tabela.add_row("18.5 - 24.9", "Peso normal")
    tabela.add_row("25.0 - 29.9", "Sobrepeso")
    tabela.add_row("30.0 - 34.9", "Obesidade Grau 1")
    tabela.add_row("35.0 - 39.9", "Obesidade Grau 2 (severa)")
    tabela.add_row("40.0 ou mais", "Obesidade Grau 3 (mórbida)")
    console.print(tabela)

def recebe_valores() -> tuple:
    """Recebe valores do peso e altura e trata exceções nos inputs."""
    while True:
        try:
            peso = float(input("Digite seu peso (em kg): "))
            break
        except ValueError:
            console.print("Você não pode usar textos ou números com vírgula. "
                          "Use apenas números válidos.", style="bold red")
        except KeyboardInterrupt:
            console.print("Programa fechado pelo usuário!", style="bold red")
            return 0, 0

    while True:
        try:
            altura = float(input("Digite sua altura (em metros): "))
            break
        except ValueError:
            console.print("Você não pode usar textos ou números com vírgula. "
                          "Use apenas números válidos.", style="bold red")
        except KeyboardInterrupt:
            console.print("Programa fechado pelo usuário!", style="bold red")
            return 0, 0

    return peso, altura

# Chamando as funções
def main():
    """Função principal para calcular o IMC e exibir a tabela."""
    peso, altura = recebe_valores()
    if peso != 0 and altura != 0:
        imc = calcula_imc(peso, altura)
        console.print(f"Seu IMC é: {imc}", style="bold green")
        exibir_tabela_imc()

if __name__ == "__main__":
    main()