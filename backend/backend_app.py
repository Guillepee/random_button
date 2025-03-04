from fastapi import FastAPI 
from pydantic import BaseModel
from enum import Enum
from class_repository import Repository

import random
import uvicorn


# Instancia de la clase FastAPI
app = FastAPI()
repository = Repository()

class RandomType(str, Enum):
    joke  = "joke"
    quote = "quote"


# Funcion que se ejecuta cuando se accede a la url raiz/joke
@app.get("/random/{type}")
async def get_joke(type: RandomType): # Type es una instancia de la clase RandomType
    if type == RandomType.joke:
        return repository.get_random_joke()
    elif type == RandomType.quote:
        return repository.get_random_quote()



if __name__ == "__main__":
    uvicorn.run("backend_app:app", host="localhost", port=8000, reload=True)


