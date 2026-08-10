import asyncio

import flet
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, TextOverflow, AppBar, Card, Row, Icon, \
    CrossAxisAlignment

from src.api_endpoints import get_planetas, get_personagens


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de API"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )