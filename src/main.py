import pandas as pd
import requests

r = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome')

if r.status_code == 200:
    df = pd.DataFrame(r.json()['dados'])