# Primeiro programa desenvolvido em Python

import flet as ft

def main(page: ft.Page):
    page.title = "Meu primeiro app Flet"
    page.padding = 20

    meu_texto = ft.Text(
        value="Hello World!",
        size=24,
        color="blue",  
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    page.add(meu_texto)

    page.add(
        ft.Text("Bem-vindo ao mundo do desenvolvimento mobile", size=16),
        ft.Text("Com Flet, você pode criar apps incríveis!", size=16, color="green")
    )

ft.app(target=main)
