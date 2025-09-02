import flet as ft

def main(page: ft.Page):
    page.title = "Criador de Perfil"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO

    # Campos do formulário
    campo_nome = ft.TextField(label="Nome completo", width=300)
    campo_idade = ft.TextField(label="Idade", width=300, keyboard_type=ft.KeyboardType.NUMBER)

    dropdown_hobby = ft.Dropdown(
        label="Hobby favorito",
        width=300,
        options=[
            ft.dropdown.Option("Leitura 📚"),
            ft.dropdown.Option("Esportes ⚽"),
            ft.dropdown.Option("Música 🎵"),
            ft.dropdown.Option("Jogos 🎮"),
            ft.dropdown.Option("Culinária 👩‍🍳"),
            ft.dropdown.Option("Arte 🎨"),
        ],
    )

    # Área do perfil criado (inicialmente oculta)
    cartao_perfil = ft.Container(
        content=ft.Text("Preencha os dados acima 👆"),
        bgcolor=ft.Colors.GREY_100,
        padding=20,
        border_radius=15,
        width=350,
        visible=False,
    )

    # Função para mostrar erro
    def mostrar_erro(msg):
        cartao_perfil.content = ft.Column([
            ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED, size=40),
            ft.Text(msg, color=ft.Colors.RED, text_align=ft.TextAlign.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        cartao_perfil.bgcolor = ft.Colors.RED_50
        cartao_perfil.visible = True
        page.update()

    # Criar perfil
    def criar_perfil(e):
        if not campo_nome.value or len(campo_nome.value) < 2:
            mostrar_erro("Nome deve ter pelo menos 2 caracteres")
            return

        if not campo_idade.value:
            mostrar_erro("Idade é obrigatória")
            return

        try:
            idade = int(campo_idade.value)
            if idade < 1 or idade > 120:
                mostrar_erro("Idade deve estar entre 1 e 120 anos")
                return
        except ValueError:
            mostrar_erro("Idade deve ser um número")
            return

        if not dropdown_hobby.value:
            mostrar_erro("Selecione um hobby")
            return

        # Definir categoria
        if idade < 18:
            categoria = "Jovem"
            cor = ft.Colors.GREEN
        elif idade < 60:
            categoria = "Adulto"
            cor = ft.Colors.BLUE
        else:
            categoria = "Experiente"
            cor = ft.Colors.PURPLE

        # Criar cartão de perfil
        cartao_perfil.content = ft.Column([
            ft.Icon(ft.Icons.PERSON, size=60, color=cor),
            ft.Text(campo_nome.value, size=20, weight=ft.FontWeight.BOLD),
            ft.Text(f"{idade} anos ({categoria})", size=14, color=ft.Colors.GREY_600),
            ft.Text(f"Hobby: {dropdown_hobby.value}", size=14),
            ft.Container(
                content=ft.Text("✅ Perfil criado com sucesso!", color=ft.Colors.WHITE),
                bgcolor=cor,
                padding=10,
                border_radius=10
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)

        cartao_perfil.bgcolor = ft.Colors.WHITE
        cartao_perfil.visible = True
        page.update()

    # Limpar campos
    def limpar_campos(e):
        campo_nome.value = ""
        campo_idade.value = ""
        dropdown_hobby.value = None
        cartao_perfil.visible = False
        page.update()

    # Botões
    botoes = ft.Row([
        ft.ElevatedButton("Criar Perfil", on_click=criar_perfil, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, width=140),
        ft.ElevatedButton("Limpar", on_click=limpar_campos, bgcolor=ft.Colors.GREY, color=ft.Colors.WHITE, width=140)
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    # Layout principal
    layout = ft.Column([
        ft.Text("📝 Criador de Perfil", size=26, weight=ft.FontWeight.BOLD),
        ft.Text("Preencha os dados abaixo para criar seu perfil personalizado!", size=14, color=ft.Colors.GREY_600),
        campo_nome,
        campo_idade,
        dropdown_hobby,
        botoes,
        cartao_perfil
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)

    page.add(layout)


# Executa como aplicativo desktop
if __name__ == "__main__":
    ft.app(target=main)