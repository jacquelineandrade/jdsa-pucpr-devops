from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests

api_url = 'https://dadosabertos.camara.leg.br'
api_endpoint = '/api/v2/deputados'
api_args = '?ordem=ASC&ordenarPor=nome'

r = requests.get(
    f'{api_url}{api_endpoint}{api_args}'
)
df = pd.DataFrame(r.json()['dados'])

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
