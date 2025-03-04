"""Frontend application for the Random Content Generator using Flet."""

import flet as ft
import random
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
CHUCK_NORRIS_API_URL = os.getenv("CHUCK_NORRIS_API_URL", "https://api.chucknorris.io/jokes/random")

def main(page: ft.Page):
    """Initialize and configure the main application page."""
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
        """Fetch a random quote from the backend API."""
        try:
            response = requests.get(f"{BACKEND_URL}/random/quote", timeout=10)
            data = response.json()
            quote = data.get("content", "No quote available")
            type = data.get("type", "Unknown")
            return quote, type
        except Exception as error:
            raise error
    
    def fetch_joke():
        """Fetch a random joke from the backend API."""
        try:
            response = requests.get(f"{BACKEND_URL}/random/joke", timeout=10)
            data = response.json()
            quote = data.get("content", "No quote available")
            type = data.get("type", "Unknown")
            return quote, type
        except Exception as error:
            raise error
    
    def fetch_random():
        """Fetch random content (quote or joke) from the backend API."""
        try:
            # Elegir aleatoriamente entre quote y joke
            content_type = random.choice(["quote", "joke"])
            response = requests.get(f"{BACKEND_URL}/random/{content_type}", timeout=10)
            data = response.json()
            quote = data.get("content", "No quote available")
            type = data.get("type", "Unknown")
            return quote, type
        except Exception as error:
            raise error
    
    def get_random_quote(e):
        """Handle button click to fetch and display random content."""
        try:
            # Obtener el identificador del botón
            button_id = e.control.data
            
            # Obtener contenido usando la función correspondiente según el botón
            if button_id == "quote":
                quote, type = fetch_quote()
            elif button_id == "joke":
                quote, type = fetch_joke()
            else:  # random
                quote, type = fetch_random()

            # Create a card for the new quote
            quote_card = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(f'"{quote}"', size=16, weight=ft.FontWeight.BOLD),
                        ft.Text(f" ({type})", italic=True)
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
    
    async def add_content(e):
        """Handle button click to fetch and add a Chuck Norris joke."""
        import time # Import time to use sleep - here por the lazy loading
        import httpx # Usamos httpx para solicitudes asíncronas
        try:
            # Obtener un chiste de Chuck Norris de la API
            async with httpx.AsyncClient() as client:
                response = await client.get(CHUCK_NORRIS_API_URL)
                if response.status_code == 200:
                    chuck_joke = response.json().get("value", "No joke available")
                    
                    # Enviar el chiste a nuestro backend
                    backend_response = await client.post(
                        f"{BACKEND_URL}/add/content",
                        json={
                            "content_type": "joke",
                            "content": chuck_joke
                        },
                    )

                    if backend_response.status_code == 200:        
                         # Create a card for the new quote
                        quote_card = ft.Card(
                            content=ft.Container(
                                content=ft.Column([
                                    ft.Text(f'"{chuck_joke}"', size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text(f" ( New Joke Added )", italic=True)
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
                else:
                    raise Exception("Failed to get Chuck Norris joke")
        except Exception as error:
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
        icon=ft.icons.LIGHTBULB_ROUNDED,
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
        icon=ft.icons.TAG_FACES_OUTLINED,
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
    
    add_content_button = ft.ElevatedButton(
        "Add Content",
        icon=ft.icons.ADD_CIRCLE_OUTLINE,
        on_click=add_content,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.padding.all(15),
        ),
        width=200
    )
    
    # Button row
    button_row = ft.Row(
        [fetch_quote_button, fetch_joke_button, fetch_random_button, add_content_button],
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

if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.WEB_BROWSER,
        port=int(os.getenv("PORT", "8550"))
    )

