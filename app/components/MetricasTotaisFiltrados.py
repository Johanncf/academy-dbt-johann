from dash import dcc, html, callback, Input, Output
from .Dropdown import Dropdown
from .MetricasCard import MetricasCard
from services import DatavisService
from utils import pedidos_totais_filtrados, quantidade_total_filtrado, total_negociado_filtrado, colors
from typing import List

def MetricasTotaisFiltrados():
    optionsDataService = DatavisService()

    nome_produto = optionsDataService.get_data(
        'SELECT DISTINCT nome_produto FROM `dbt_adventure_works.vendas`'
    )['nome_produto'].to_list()

    tipo_cartao = optionsDataService.get_data(
        'SELECT DISTINCT tipo_cartao FROM `dbt_adventure_works.vendas`'
    )['tipo_cartao'].to_list()

    data_pedido = optionsDataService.get_data(
        'SELECT DISTINCT data_pedido FROM `dbt_adventure_works.vendas` ORDER BY data_pedido DESC'
    )['data_pedido'].to_list()

    nome_cliente = optionsDataService.get_data(
        'SELECT DISTINCT nome_cliente FROM `dbt_adventure_works.vendas`'
    )['nome_cliente'].to_list()

    status_pedido = optionsDataService.get_data(
        'SELECT DISTINCT status_pedido FROM `dbt_adventure_works.vendas`'
    )['status_pedido'].to_list()
    
    cidade = optionsDataService.get_data(
        'SELECT DISTINCT cidade FROM `dbt_adventure_works.vendas`'
    )['cidade'].to_list()
    
    nome_estado = optionsDataService.get_data(
        'SELECT DISTINCT nome_estado FROM `dbt_adventure_works.vendas`'
    )['nome_estado'].to_list()

    sigla_3 = optionsDataService.get_data(
        'SELECT DISTINCT sigla_3 FROM `dbt_adventure_works.vendas`'
    )['sigla_3'].to_list()


    return html.Div(children=[
        html.Div([
            MetricasCard(title='Pedidos Totais', id='pedidos_totais'),
            MetricasCard(title='Quantidade Comprada Total', id='quantidade_total'),
            MetricasCard(title='Valor Total Negociado', id='valor_total')
        ],
        style={
            'display': 'flex', 
            'justify-content': 'space-between',
            'margin-bottom': '30px'
        }),
        html.Div([
            html.Div(
                Dropdown('totais_produto', [{'name': item, 'value': item} for item in nome_produto], placeholder='Produto'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_tipo_cartao', [{'name': item, 'value': item} for item in tipo_cartao], placeholder='Tipo de Cartão'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_data_pedido', [{'name': item, 'value': item} for item in data_pedido], placeholder='Data do Pedido'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_nome_cliente', [{'name': item, 'value': item} for item in nome_cliente], placeholder='Cliente'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_status_pedido', [{'name': item, 'value': item} for item in status_pedido], placeholder='Status do Pedido'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_cidade', [{'name': item, 'value': item} for item in cidade], placeholder='Cidade'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_nome_estado', [{'name': item, 'value': item} for item in nome_estado], placeholder='Estado'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_sigla_3', [{'name': item, 'value': item} for item in sigla_3], placeholder='País'),
                style={'width': '100%'}
            )
        ], 
        style={'display': 'flex', 'width': '100%'})
    ],
    style={
        'marginTop': '100px', 
        'width': '100%',
        'display': 'flex',
        'flexDirection': 'column',
        'backgroundColor': colors['dark-bg-0']
    })


@callback(
    Output('pedidos_totais', 'children'),
    Input('totais_produto', 'value'),
    Input('totais_tipo_cartao', 'value'),
    Input('totais_data_pedido', 'value'),
    Input('totais_nome_cliente', 'value'),
    Input('totais_status_pedido', 'value'),
    Input('totais_cidade', 'value'),
    Input('totais_nome_estado', 'value'),
    Input('totais_sigla_3', 'value')
)
def render_pedidos(produto, tipo_cartao, data, cliente, status, cidade, estado, pais):
    datavisService = DatavisService()
    return datavisService.get_data(pedidos_totais_filtrados(produto, tipo_cartao, data, cliente, status, cidade, estado, pais))['total'][0]

@callback(
    Output('quantidade_total', 'children'),
    Input('totais_produto', 'value'),
    Input('totais_tipo_cartao', 'value'),
    Input('totais_data_pedido', 'value'),
    Input('totais_nome_cliente', 'value'),
    Input('totais_status_pedido', 'value'),
    Input('totais_cidade', 'value'),
    Input('totais_nome_estado', 'value'),
    Input('totais_sigla_3', 'value')
)
def render_quantidade(produto, tipo_cartao, data, cliente, status, cidade, estado, pais):
    datavisService = DatavisService()
    return datavisService.get_data(quantidade_total_filtrado(produto, tipo_cartao, data, cliente, status, cidade, estado, pais))['total'][0]

@callback(
    Output('valor_total', 'children'),
    Input('totais_produto', 'value'),
    Input('totais_tipo_cartao', 'value'),
    Input('totais_data_pedido', 'value'),
    Input('totais_nome_cliente', 'value'),
    Input('totais_status_pedido', 'value'),
    Input('totais_cidade', 'value'),
    Input('totais_nome_estado', 'value'),
    Input('totais_sigla_3', 'value')
)
def render_total_negociado(produto, tipo_cartao, data, cliente, status, cidade, estado, pais):
    datavisService = DatavisService()
    return datavisService.get_data(total_negociado_filtrado(produto, tipo_cartao, data, cliente, status, cidade, estado, pais))['total'][0]