import flet as ft

# Lista global para armazenar os produtos
produtos = []

def main(page: ft.Page):
    page.title = "Desafio - Cadastro de Produtos"
    page.window_width = 800
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT

    # Campos de entrada
    nome = ft.TextField(label="Nome do Produto", width=300)
    preco = ft.TextField(label="Preço", width=150)
    categoria = ft.Dropdown(
        label="Categoria",
        width=200,
        options=[
            ft.dropdown.Option("Alimento"),
            ft.dropdown.Option("Bebida"),
            ft.dropdown.Option("Higiene"),
            ft.dropdown.Option("Limpeza"),
        ],
    )

    # Tabela de produtos
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Preço")),
            ft.DataColumn(ft.Text("Categoria")),
        ],
        rows=[],
    )

    def atualizar_tabela():
        tabela.rows.clear()
        for p in produtos:
            tabela.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(p["nome"])),
                        ft.DataCell(ft.Text(f"R$ {p['preco']}")),
                        ft.DataCell(ft.Text(p["categoria"])),
                    ]
                )
            )
        page.update()

    def adicionar_produto(e):
        if nome.value and preco.value and categoria.value:
            produtos.append(
                {"nome": nome.value, "preco": preco.value, "categoria": categoria.value}
            )
            nome.value = ""
            preco.value = ""
            categoria.value = None
            atualizar_tabela()
            page.update()

    # Botão para adicionar
    btn_add = ft.ElevatedButton("Adicionar Produto", on_click=adicionar_produto)

    # Layout
    page.add(
        ft.Column(
            [
                ft.Row([nome, preco, categoria, btn_add]),
                ft.Container(content=tabela, expand=True, padding=20),
            ],
            expand=True,
        )
    )

    atualizar_tabela()


if __name__ == "__main__":
    ft.app(target=main)  # Executa como aplicativo de desktop
