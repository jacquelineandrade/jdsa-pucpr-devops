from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests

API_URL = 'https://dadosabertos.camara.leg.br'
API_ENDPOINT = '/api/v2/deputados'
API_ARGS = '?ordem=ASC&ordenarPor=nome'


def get_data(
    api_url: str,
    api_endpoint: str,
    api_args: str
) -> dict:
    """Realiza a requisição dos dados na API e retorna uma dict."""

    r = requests.get(
        f'{api_url}{api_endpoint}{api_args}'
    )
    return r.json()


base_data = get_data(API_URL, API_ENDPOINT, API_ARGS)
df = pd.DataFrame(base_data['dados'])

app = Dash()

app.layout = [
    html.H1(
        children='Deputados Federais - Visão Geral',
        style={'textAlign': 'center', 'font-family': 'Arial'}
    ),
    dcc.Graph(
        figure=px.histogram(
            df,
            title='Qtd de Deputados por UF',
            x='siglaUf',
            y='id',
            histfunc='count',
            category_orders={'siglaUf': df['siglaUf'].value_counts().index},
            text_auto=True,
            labels={'siglaUf': 'UF'}
        )
    ),
    dcc.Graph(
        figure=px.histogram(
            df,
            title='Qtd de Deputados por Partido',
            x='siglaPartido',
            y='id',
            histfunc='count',
            category_orders={
                'siglaPartido': df['siglaPartido'].value_counts().index
            },
            text_auto=True,
            labels={'siglaPartido': 'Partido'}
        )
    )
]

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8050)
