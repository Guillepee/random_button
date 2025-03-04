"""Backend API for the Random Content Generator."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from database_repository import DatabaseRepository
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Instancia de la clase FastAPI
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:8080,http://localhost:8550").split(","),
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

# Initialize repository with database path from environment
repository = DatabaseRepository(os.getenv("DB_PATH", "./repository.db"))

class RandomType(str, Enum):
    """Enumeration class for different types of random content.

    Attributes:
        JOKE (str): Represents a joke type
        QUOTE (str): Represents a quote type
    """
    JOKE = "joke"
    QUOTE = "quote"


# Funcion que se ejecuta cuando se accede a la url raiz/joke
@app.get("/random/{content_type}")
async def get_result(content_type: RandomType):  # content_type es una instancia
    """Get random content (joke or quote) based on the specified type."""
    if content_type == RandomType.JOKE:
        return repository.get_random_joke()
    elif content_type == RandomType.QUOTE:
        return repository.get_random_quote()

class ContentItem(BaseModel):
    """Model for content items to be added to the repository.
    
    Attributes:
        content_type (RandomType): Type of content (joke or quote)
        content (str): The actual content text
    """
    content_type: RandomType
    content: str

@app.post("/add/content")
async def add_content(item: ContentItem):
    """Add new content (joke or quote) to the repository.
    
    Args:
        item (ContentItem): The content item to be added
        
    Returns:
        dict: A confirmation message with the added content
    """
    if item.content_type == RandomType.JOKE:
        repository.add_content("joke", item.content)
        return {"message": "Joke added successfully", "content": item.content}
    elif item.content_type == RandomType.QUOTE:
        repository.add_content("quote", item.content)
        return {"message": "Quote added successfully", "content": item.content}

if __name__ == "__main__":
    uvicorn.run(
        "backend_app:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        reload=os.getenv("DEBUG", "False").lower() == "true"
    )