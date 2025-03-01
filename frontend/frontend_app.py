import flet as ft
import time
import os

import requests
from datetime import datetime

def main(page: ft.Page):
    page.title = "Random Quote Generator"
    page.window.maximized = True
    page.theme_mode = ft.ThemeMode.DARK
    
    # Container to hold all quotes
    quotes_container = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        height=500,
        width=600
    )
    
    def get_random_quote(e):
        try:
            # API request to get a random quote
            response = requests.get("http://localhost:8000/random/joke")
            data = response.json()
            
            quote = data.get("content", "No quote available")
            type = data.get("type", "Unknown")
            timestamp = datetime.now().strftime("%H:%M:%S")
            

            # Create a card for the new quote
            quote_card = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(f'"{quote}"', size=16, weight=ft.FontWeight.BOLD),
                        ft.Text(f"- {type}", italic=True),
                        ft.Text(f"Retrieved at: {timestamp}", size=12, color=ft.colors.GREY_400)
                    ]),
                    padding=15,
                    border_radius=10
                ),
                elevation=5,
                margin=ft.margin.only(bottom=10)
            )
            
            # Add the new quote at the beginning of the list
            quotes_container.controls.insert(0, quote_card)
            page.update()
            
        except Exception as error:
            # Show error message if request fails
            error_card = ft.Card(
                content=ft.Container(
                    content=ft.Text(f"Error: {str(error)}", color=ft.colors.RED_500),
                    padding=15
                ),
                elevation=5,
                margin=ft.margin.only(bottom=10)
            )
            quotes_container.controls.insert(0, error_card)
            page.update()
    
    # Create the button to fetch quotes
    fetch_button = ft.ElevatedButton(
        "Get Random Quote",
        icon=ft.icons.TAG_FACES_SHARP,
        on_click=get_random_quote,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.padding.all(15),
        ),
        width=200
    )
    
    # Main layout
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Random Quote Generator", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Click the button to get a random quote", size=16, color=ft.colors.GREY_400),
                ft.Divider(),
                fetch_button,
                ft.Divider(),
                quotes_container
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20),
            padding=30,
            alignment=ft.alignment.center
        )
    )

ft.app(main)

