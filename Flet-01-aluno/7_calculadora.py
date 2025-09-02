import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Simples"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    # Campos e elementos
    numero1 = ft.TextField(
        label="Primeiro número", 
        width=200, 
        keyboard_type=ft.KeyboardType.NUMBER
    )
    numero2 = ft.TextField(
        label="Segundo número", 
        width=200, 
        keyboard_type=ft.KeyboardType.NUMBER
    )
    operacao = ft.Dropdown(
        label="Operação", 
        width=200,
        options=[
            ft.dropdown.Option("Soma", "Soma"),
            ft.dropdown.Option("Subtração", "Subtração"),
            ft.dropdown.Option("Multiplicação", "Multiplicação"),
            ft.dropdown.Option("Divisão", "Divisão")
        ]
    )
    resultado = ft.Text(
        "Resultado aparecerá aqui", 
        size=20, 
        text_align=ft.TextAlign.CENTER, 
        color="grey"
    )

    # Funções
    def calcular(e):
        try:
            num1, num2, op = float(numero1.value), float(numero2.value), operacao.value

            if not op:
                resultado.value, resultado.color = "⚠️ Selecione uma operação!", "orange"
            elif op == "Divisão" and num2 == 0:
                resultado.value, resultado.color = "❌ Erro: Divisão por zero!", "red"
            else:
                simbolos = {
                    "Soma": ("+", num1 + num2),
                    "Subtração": ("-", num1 - num2),
                    "Multiplicação": ("×", num1 * num2),
                    "Divisão": ("/", num1 / num2)
                }
                simbolo, res = simbolos[op]
                resultado.value, resultado.color = f"{num1} {simbolo} {num2} = {res:.2f}", "green"
        except ValueError:
            resultado.value, resultado.color = "❌ Digite números válidos!", "red"
        page.update()

    def limpar(e):
        numero1.value = numero2.value = operacao.value = ""
        resultado.value, resultado.color = "Campos limpos! ✨", "blue"
        page.update()

    # Interface
    page.add(
        ft.Column([
            ft.Text("🧮 Calculadora Simples", size=24, weight=ft.FontWeight.BOLD),
            numero1,
            numero2,
            operacao,
            ft.Row([
                ft.ElevatedButton(
                    "✅ Calcular", 
                    on_click=calcular, 
                    width=150, 
                    bgcolor="green", 
                    color="white"
                ),
                ft.ElevatedButton(
                    "🧹 Limpar", 
                    on_click=limpar, 
                    width=150,
                    bgcolor="grey", 
                    color="white"
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
            resultado
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
    )

ft.app(target=main)
