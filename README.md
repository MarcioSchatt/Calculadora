# Calculadora em Python com Tkinter

Este projeto é uma **calculadora simples** feita em Python utilizando a biblioteca Tkinter para a interface gráfica. Esta aplicação permite que o usuário realize operações matemáticas básicas como adição, subtração, multiplicação e divisão. Além de incluir uma funcionalidade para limpar a entrada e calcular resultados.

## Funcionalidades

- **Operações Matemáticas Básicas**: Suporta as operações de adição *+*, subtração *-*, multiplicação *\** e divisão */*.
- **Limpar Entrada**: O botão *C* permite limpar a tela de entrada.
- **Calculadora Interativa**: Permite interação tanto com os botões na interface gráfica quanto com a tecla Enter para calcular a expressão digitada.
- **Tratamento de Erros**: Caso o usuário insira uma expressão inválida, a calculadora exibe uma mensagem de erro.

## Técnologias Utilizadas

- **Python**: Linguagem de programação usada para criar a lógica da calculadora.
- **Tkinter**: Biblioteca padrão do Python para criar interfaces gráficas.

## Como Funciona

O código usa Tkinter para criar uma interface gráfica simples.

- **Entrada de Dados**: O usuário insere uma expressão matemática na área de entrada.
- **Botões**: Os botões são organizados em um layout de matriz, onde cada botão corresponde a um número, operador ou função de controle (limpar ou calcular).
- **Ação dos Botões**: A função *on_click* manipula os cliques nos botões. Para o botão de igual *=*, é feito o cálculo da expressão, e em caso de erro, é exibida uma mensagem de erro. O botão *C* limpa a tela de entrada.
- **Tecla Enter**: O pressionamento da tecla *Enter* é configurado para realizar o mesmo cálculo que o botão "=".

## Contribuições

**Se você quiser contribuir para este projeto, fique à vontade para abrir issues ou enviar pull requests. Toda contribuição sempre será bem-vinda!**

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).