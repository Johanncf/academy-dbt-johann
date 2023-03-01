from dash import dcc, html, callback, Input, Output
from .Dropdown import Dropdown
from .MetricasCard import MetricasCard
from services import DatavisService
from utils import pedidos_totais_filtrados, quantidade_total_filtrado, total_negociado_filtrado, colors
from typing import List

def MetricasTotaisFiltrados(dimensoes: dict):
    optionsDataService = DatavisService()

    return html.Div(children=[
        html.Div([
            MetricasCard(title='Pedidos Totais', id='pedidos_totais'),
            MetricasCard(title='Quantidade Total Comprada', id='quantidade_total'),
            MetricasCard(title='Valor Total Negociado', id='valor_total')
        ],
        style={
            'display': 'flex', 
            'justify-content': 'space-between',
            'margin-bottom': '30px'
        }),
        html.Div([
            html.Div(
                Dropdown('totais_produto', [{'name': item, 'value': item} for item in dimensoes['nome_produto']], placeholder='Produto'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_tipo_cartao', [{'name': item, 'value': item} for item in dimensoes['tipo_cartao']], placeholder='Tipo de Cartão'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_data_pedido', [{'name': item, 'value': item} for item in dimensoes['data_pedido']], placeholder='Data do Pedido'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_nome_cliente', [{'name': item, 'value': item} for item in dimensoes['nome_cliente']], placeholder='Cliente'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_status_pedido', [{'name': item, 'value': item} for item in dimensoes['status_pedido']], placeholder='Status do Pedido'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_cidade', [{'name': item, 'value': item} for item in dimensoes['cidade']], placeholder='Cidade'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_nome_estado', [{'name': item, 'value': item} for item in dimensoes['nome_estado']], placeholder='Estado'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('totais_sigla_3', [{'name': item, 'value': item} for item in dimensoes['sigla_3']], placeholder='País'),
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