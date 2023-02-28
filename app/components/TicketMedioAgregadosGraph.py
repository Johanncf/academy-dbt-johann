from dash import dcc, html, callback, Input, Output
from .Dropdown import Dropdown
from services import DatavisService
from utils import ticket_medio_por_dimensao, write_title, colors
from typing import List

def TicketMedioAgregadosGraph():
    optionsDataService = DatavisService()

    ano_options = optionsDataService.get_data(
        'SELECT DISTINCT ano_pedido ano FROM `dbt_adventure_works.vendas` ORDER BY ano'
    )['ano'].to_list()

    mes_options = optionsDataService.get_data(
        'SELECT DISTINCT mes_pedido mes FROM `dbt_adventure_works.vendas` ORDER BY mes'
    )['mes'].to_list()

    cidade_options = optionsDataService.get_data(
        'SELECT DISTINCT cidade FROM `dbt_adventure_works.vendas`'
    )['cidade'].to_list()

    estado_options = optionsDataService.get_data(
        'SELECT DISTINCT nome_estado estado FROM `dbt_adventure_works.vendas`'
    )['estado'].to_list()

    pais_options = optionsDataService.get_data(
        'SELECT DISTINCT sigla_3 pais FROM `dbt_adventure_works.vendas`'
    )['pais'].to_list()


    return html.Div(children=[
        dcc.Graph(id='ticket_medio_agregados'),
        html.Div([
            html.Div(
                Dropdown('ticket_ano', [{'name': item, 'value': item} for item in ano_options]),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('ticket_mes', [{'name': item, 'value': item} for item in mes_options]),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('ticket_cidade', [{'name': item, 'value': item} for item in cidade_options]),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('ticket_estado', [{'name': item, 'value': item} for item in estado_options]),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('ticket_pais', [{'name': item, 'value': item} for item in pais_options]),
                style={'width': '100%'}
            )
        ], 
        style={'display': 'flex', 'width': '100%'})
    ],
    style={'marginTop': '100px', 'width': '100%'})


@callback(
    Output('ticket_medio_agregados', 'figure'),
    Input('ticket_ano', 'value'),
    Input('ticket_mes', 'value'),
    Input('ticket_cidade', 'value'),
    Input('ticket_estado', 'value'),
    Input('ticket_pais', 'value')
)
def render_graph(ano, mes, cidade, estado, pais):
    datavisService = DatavisService()
    datavisService.get_data(ticket_medio_por_dimensao(ano, mes, cidade, estado, pais))
    return datavisService.make_bar_graph(
        x='total', 
        y='nome_produto', 
        title='Produtos com maior ticket médio', 
        style_dict=colors, 
        orientation='h')