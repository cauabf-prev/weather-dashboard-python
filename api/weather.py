#instalar bibliotecas nescessarias!
import os
import requests
from dotenv import load_dotenv

#aqui o load_dotenv vai ler o dict da pasta env
load_dotenv()

#os.getenv vai ler a chave da api e guardar na variavel api_key
api_key = os.getenv("API_KEY")
LINGUAGE = "pt_br"
UNITS = "metric"


#Aqui vamos criar a funcion que vai buscar o clima da cidade.
def buscar_clima(cidade):
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units={UNITS}&lang={LINGUAGE}")
    resposta = requests.get(url)
    dados = resposta.json()
    status_api = resposta.status_code
    if status_api == 404:
        return(None)
    
    return({
        "temperatura":(dados["main"]["temp"]),
        "cidade":(dados["name"]),
        "umidade":(dados["main"]["humidity"]),
        "descrição":(dados["weather"][0]["description"])
        (status_api)
        })
