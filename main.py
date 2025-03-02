import tkinter as tk
from tkinter import messagebox


def on_click(txt_btn: str, entrada: tk.StringVar) -> None:
    """
    Manipula a entrada quando um botão é pressionado.

    Args:
        txt_btn (str): O texto exibido no botão pressionado.
        entrada (tk.StringVar): Variável de controle do campo de entrada.
    """
    if txt_btn == "C":
        entrada.set("")
    elif txt_btn == "=":
        try:
            entrada.set(eval(entrada.get()))
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida")
    else:
        entrada.set(entrada.get() + txt_btn)


def on_enter(entrada: tk.StringVar) -> None:
    """
    Executa a mesma ação do botão "=" quando a tecla Enter é pressionada.

    Args:
        entrada (tk.StringVar): Variável de controle do campo de entrada.
    """
    on_click("=", entrada)


def criar_botoes(janela: tk.Tk, ent: tk.StringVar) -> None:
    """
    Cria e organiza os botões da calculadora na interface gráfica.

    Args:
        janela (tk.Tk): A janela principal da aplicação.
        ent (tk.StringVar): Variável de controle do campo de entrada.
    """
    botoes = [("7", "8", "9", "/"), ("4", "5", "6", "*"),
              ("1", "2", "3", "-"), ("C", "0", "=", "+")]

    quadro = tk.Frame(janela)
    quadro.pack(padx=5, pady=5)

    for linha in botoes:
        quadro_linha = tk.Frame(quadro)
        quadro_linha.pack(expand=True, fill="both", pady=2)
        for texto in linha:
            botao = tk.Button(
                quadro_linha, text=texto, font=("Arial", 18), width=5, height=2, command=lambda t=texto: on_click(t, ent))
            botao.pack(side="left", expand=True, fill="both", padx=2, pady=2)


def main() -> None:
    """
    Inicializa a aplicação da calculadora criando a interface gráfica.
    """
    janela = tk.Tk()
    janela.title("Calculadora")
    janela.geometry("400x400")

    entrada = tk.StringVar()
    ent = tk.Entry(
        janela, textvariable=entrada, font=("Arial", 20), justify="right", bd=10, relief=tk.GROOVE)
    ent.pack(fill="both", padx=10, pady=10)
    ent.focus()
    ent.bind("<Return>", lambda event: on_enter(entrada))

    criar_botoes(janela, entrada)

    janela.mainloop()


if __name__ == "__main__":
    main()
