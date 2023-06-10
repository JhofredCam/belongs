import pandas as pd
from fastapi import FastAPI
import ast

# http://127.0.0.1:8000/

app = FastAPI()

movies = pd.read_csv("belongs_to_collection.csv")

@app.get("{row}")
def get_row(row:int) -> str:
    """
    Devuelve la cantidad de películas estrenadas en un mes específico.

    Parámetros:
    - month (str): El mes para el cual se desea obtener la cantidad de películas estrenadas.

    Retorna:
    Una cadena de texto que indica la cantidad de películas estrenadas en el mes especificado.

    """
    return movies[row].to_dict()