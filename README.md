# Calculadora em Python com Tkinter

Este projeto é uma **calculadora simples** feita em Python utilizando a biblioteca Tkinter para a interface gráfica. Esta aplicação permite que o usuário realize operações matemáticas básicas como adição, subtração, multiplicação e divisão. Além de incluir uma funcionalidade para limpar a entrada e calcular resultados.

## Funcionalidades

- **Operações Matemáticas Básicas**: Suporta as operações de adição ***+***, subtração ***-***, multiplicação ***\**** e divisão ***/***.
- **Limpar Entrada**: O botão ***C*** permite limpar a tela de entrada.
- **Calculadora Interativa**: Permite interação tanto com os botões na interface gráfica quanto com a tecla Enter para calcular a expressão digitada.
- **Tratamento de Erros**: Caso o usuário insira uma expressão inválida, a calculadora exibe uma mensagem de erro.

## Técnologias Utilizadas

- **Python**: Linguagem de programação usada para criar a lógica da calculadora.
- **Tkinter**: Biblioteca padrão do Python para criar interfaces gráficas.

## Como Executar

Para começar a usar a calculadora, siga os passos abaixo:

- **Clone o Repositório**: Primeiro, clone o repositório para o seu computador usando o Git. No Terminal, execute o seguinte comando:

```
git clone https://github.com/seuusuario/nome-do-repositorio.git
```

Substitua ***seuusuario*** e ***nome-do-repositorio*** pelo seu **nome de usuário do GitHub** e pelo **nome do repositório**.

- **Instale o Tkinter**: O Tkinter é uma biblioteca padrão do Python para criar interfaces gráficas. Caso não o tenha instalado, precisa apenas rodar o seguinte comando para instalá-lo:

No Windows ou Linux (geralmente já vem instalado):

```
pip install tk
```

No ***macOS***, o Tkinter já deve estar incluído com a instalação do Python. Caso não esteja, use o seguinte comando:

```
brew install python-tk
```

- **Execute o Programa**: Após clonar o repositório e instalar o Tkinter, navegue até o diretório onde o repositório foi clonado e execute o seguinte comando para rodar a calculadora:

```
python calculadora.py
```

A janela da calculadora será aberta, e você poderá começar a usá-la.

## Como Funciona

O código usa Tkinter para criar uma interface gráfica simples.

- **Entrada de Dados**: O usuário insere uma expressão matemática na área de entrada.
- **Botões**: Os botões são organizados em um layout de matriz, onde cada botão corresponde a um número, operador ou função de controle (limpar ou calcular).
- **Ação dos Botões**: A função ***on_click*** manipula os cliques nos botões. Para o botão de igual ***=***, é feito o cálculo da expressão, e em caso de erro, é exibida uma mensagem de erro. O botão ***C*** limpa a tela de entrada.
- **Tecla Enter**: O pressionamento da tecla ***Enter*** é configurado para realizar o mesmo cálculo que o botão ***=***.

## Contribuições

**Se você quiser contribuir para este projeto, fique à vontade para abrir issues ou enviar pull requests. Toda contribuição sempre será bem-vinda!**

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE.txt).