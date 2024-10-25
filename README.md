# Programa de Cálculo do IMC

## Métodos

### Ferramentas Utilizadas
O desenvolvimento do programa foi realizado no Google Cloud Shell Editor, que permite executar e editar código nos servidores da Google Cloud Platform. A linguagem de programação escolhida para a implementação do programa foi Python, devido à sua simplicidade e versatilidade, facilitando o desenvolvimento de projetos variados, desde aplicações matemáticas até ferramentas de automação e inteligência artificial.

### Estrutura e Funcionamento do Programa
O programa foi estruturado em três partes principais:

1. **Função de Cálculo do IMC**:
    - Uma função `calcula_IMC` foi criada para receber o peso (em kg) e a altura do usuário e calcular o IMC. O cálculo do IMC utiliza a fórmula:
      ```text
      IMC = PESO / (ALTURA * ALTURA)
      ```
    - O valor resultante é arredondado para duas casas decimais para facilitar a compreensão.

2. **Exibição da Tabela de Classificação de IMC**:
    - Outra função, `exibir_tabela_imc`, exibe uma tabela com as classificações de IMC, utilizando a biblioteca `rich` para fornecer uma interface visual clara. As categorias incluem "Abaixo do peso", "Peso normal", "Sobrepeso" e os diferentes graus de obesidade, conforme as diretrizes padrão de saúde.

3. **Recebimento de Dados do Usuário e Tratamento de Erros**:
    - Para coletar dados do usuário (peso e altura), uma função chamada `recebe_valores` foi implementada. Ela inclui mecanismos de tratamento de exceções para garantir que apenas valores numéricos válidos sejam aceitos, evitando erros no cálculo.

### Lógica de Fluxo do Programa
O programa é executado da seguinte forma:
1. Os dados de peso e altura são recebidos do usuário.
2. A função `calcula_IMC` processa esses valores e retorna o IMC arredondado.
3. Em seguida, o IMC calculado e a tabela de classificação são exibidos ao usuário, permitindo que ele compreenda sua posição na escala de IMC.

### Resultados
O programa foi capaz de calcular o IMC do usuário e exibir uma tabela de classificação que ajuda na interpretação do resultado. O uso da biblioteca `rich` facilitou a formatação da tabela, proporcionando uma visualização organizada das classificações.
