from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import flet
from flet import Page, ThemeMode, Text, Button, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, \
    Colors, \
    FontWeight, Card, Image, TextOverflow, ListView, Pagelet, NavigationBar, NavigationBarDestination, Icons, \
    ScrollMode, View, Row, Icon
from flet.controls import page
from flet.controls.core import list_view

from api_endpoints import get_produtos


def main(page: flet.Page):

    #Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    def montar_lista_produtos():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_produtos()
        for item in lista_dados["products"]:
            list_view.controls.append(
                Card(
                    height=250,
                    content=Column([
                        Image(src=item["images"][0], width=60, height=100),
                        Text(item["title"], weight=FontWeight.BOLD),
                        Text(f'Categoria: {item['category']}', overflow=TextOverflow.ELLIPSIS),
                        Text(f'Valor:{item['price']}', overflow=TextOverflow.ELLIPSIS),
                        Row([
                            Text(f'{item['rating']}', overflow=TextOverflow.ELLIPSIS),
                            Icon( Icons.STAR)
                        ]
                        ),
                    ],
                        margin=8,
                        horizontal_alignment=CrossAxisAlignment.CENTER,

                    ),
                    bgcolor=Colors.PINK_600,
                )
            )

    # Gerenciar as telas(routes)
    def route_change():

        montar_lista_produtos()

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Produtos", weight=FontWeight.BOLD),
                        bgcolor=Colors.PINK_600
                    ),
                    Column([
                        pagelet,
                    ])
                ],
                padding=0
            )
        )

        # Voltar

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    list_view = ListView(height=500)

    pagelet = Pagelet(
        navigation_bar=NavigationBar(
            destinations=[
                NavigationBarDestination(icon=Icons.DATA_OBJECT, label="Produtos"),
                NavigationBarDestination(icon=Icons.DATA_OBJECT, label="Produtos")
            ],
        ),
        content=Column([
            list_view,
        ],
            scroll=ScrollMode.HIDDEN,
            height=500
        ),
        height=600
    )

    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)