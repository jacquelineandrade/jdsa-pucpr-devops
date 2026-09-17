import pytest
import requests_mock
from src.app import get_data

def test_get_data_sucesso(requests_mock):
    full_url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'

    false_response = {
        'dados': [
            {
                'id': 111111,
                'uri': 'https://dadosabertos.camara.leg.br/api/v2/deputados/111111',
                'nome': 'Fulano da Silva',
                'siglaPartido': 'PT - Partido dos Testes',
                'uriPartido': 'https://dadosabertos.camara.leg.br/api/v2/partidos/36899',
                'siglaUf': 'PR',
                'idLegislatura': 57,
                'urlFoto': 'https://www.camara.leg.br/internet/deputado/bandep/111111.jpg',
                'email': 'dep.fulanosilva@camara.leg.br'
            },
            {
                'id': 222222,
                'uri': 'https://dadosabertos.camara.leg.br/api/v2/deputados/222222',
                'nome': 'Ciclano dos Santos',
                'siglaPartido': 'PSOL - Partido do Software Livre',
                'uriPartido': 'https://dadosabertos.camara.leg.br/api/v2/partidos/36899',
                'siglaUf': 'SP',
                'idLegislatura': 57,
                'urlFoto': 'https://www.camara.leg.br/internet/deputado/bandep/222222.jpg',
                'email': 'dep.ciclanosantos@camara.leg.br'
            }
        ]
    }

    requests_mock.get(full_url, json=false_response, status_code=200)
    
    results = get_data(
        'https://dadosabertos.camara.leg.br', 
        '/api/v2/deputados', 
        '?ordem=ASC&ordenarPor=nome'
    )
    
    assert results == false_response
    assert results['dados'][0]['nome'] == 'Fulano da Silva'
    assert results['dados'][0]['siglaPartido'] == 'PT - Partido dos Testes'
    assert results['dados'][0]['siglaUf'] == 'PR'