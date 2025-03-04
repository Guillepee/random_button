import flet as ft
import random
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

    def fetch_quote():
        try:
            response = requests.get("http://localhost:8000/random/quote")
            data = response.json()
            quote = data.get("content", "No quote available")
            type = data.get("type", "Unknown")
            timestamp = datetime.now().strftime("%H:%M:%S")
            return quote, type, timestamp
        except Exception as error:
            raise error
    
    def fetch_joke():
        try:
            response = requests.get("http://localhost:8000/random/joke")
            data = response.json()
            quote = data.get("content", "No quote available")
            type = data.get("type", "Unknown")
            timestamp = datetime.now().strftime("%H:%M:%S")
            return quote, type, timestamp
        except Exception as error:
            raise error
    
    def fetch_random():
        try:
            # Elegir aleatoriamente entre quote y joke
            content_type = random.choice(["quote", "joke"])
            response = requests.get(f"http://localhost:8000/random/{content_type}")
            data = response.json()
            quote = data.get("content", "No quote available")
            type = data.get("type", "Unknown")
            timestamp = datetime.now().strftime("%H:%M:%S")
            return quote, type, timestamp
        except Exception as error:
            raise error
    
    def get_random_quote(e):
        try:
            # Obtener el identificador del botón
            button_id = e.control.data
            
            # Obtener contenido usando la función correspondiente según el botón
            if button_id == "quote":
                quote, type, timestamp = fetch_quote()
            elif button_id == "joke":
                quote, type, timestamp = fetch_joke()
            else:  # random
                quote, type, timestamp = fetch_random()

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
    
    # Create the buttons to get content
    fetch_quote_button = ft.ElevatedButton(
        "Get Quote",
        icon=ft.icons.TAG_FACES_SHARP,
        on_click=get_random_quote,
        data="quote",  # Identificador para el botón de quotes
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.padding.all(15),
        ),
        width=200
    )
    
    fetch_joke_button = ft.ElevatedButton(
        "Get Joke",
        icon=ft.icons.TAG_FACES_SHARP,
        on_click=get_random_quote,
        data="joke",  # Identificador para el botón de jokes
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.padding.all(15),
        ),
        width=200
    )
    
    fetch_random_button = ft.ElevatedButton(
        "Get Random",
        icon=ft.icons.TAG_FACES_SHARP,
        on_click=get_random_quote,
        data="random",  # Identificador para el botón de random
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.padding.all(15),
        ),
        width=200
    )
    
    # Button row
    button_row = ft.Row(
        [fetch_quote_button, fetch_joke_button, fetch_random_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )
    
    # Main layout
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Random Quote Generator", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Click the button to get a random quote", size=16, color=ft.colors.GREY_400),
                ft.Divider(),
                button_row,
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

