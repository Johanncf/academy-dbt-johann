from dash import dcc, html, callback, Input, Output
from .Dropdown import Dropdown
from services import DatavisService
from utils import melhores_clientes_total_negociado_por_dimensao, clientes_vs_lojas_total_negociado_por_dimensao, \
    melhores_lojas_total_negociado_por_dimensao, dimensoes_categorias, colors

def MelhoresClientesGraph(dimensoes: dict):
    return html.Div(children=[
        html.Div([
            html.Div([
                dcc.Graph(id='pessoa_fisica_vs_lojas'),
            ], style={'width': '25%'}),
            html.Div([
                dcc.Graph(id='melhores_clientes', style={'width': '50%'}),
                dcc.Graph(id='melhores_lojas', style={'width': '50%'})
            ], style={'display': 'flex', 'width': '75%'})
        ], 
        style={'display': 'flex', 'width': '100%'}),
        html.Div([
            html.Div(
                Dropdown('melhores_clientes_produto', [{'name': item, 'value': item} for item in dimensoes['nome_produto']], placeholder='Produto'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('melhores_clientes_cartao', [{'name': item, 'value': item} for item in dimensoes['tipo_cartao']], placeholder='Tipo de Cartão'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('melhores_clientes_data_pedido', [{'name': item, 'value': item} for item in dimensoes['data_pedido']], placeholder='Data do Pedido'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('melhores_clientes_motivo_venda', [{'name': item, 'value': item} for item in dimensoes['motivo_venda']], placeholder='Motivo da Venda'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('melhores_clientes_cidade', [{'name': item, 'value': item} for item in dimensoes['cidade']], placeholder='Cidade'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('melhores_clientes_nome_estado', [{'name': item, 'value': item} for item in dimensoes['nome_estado']], placeholder='Estado'),
                style={'width': '100%'}
            ),
            html.Div(
                Dropdown('melhores_clientes_sigla_3', [{'name': item, 'value': item} for item in dimensoes['sigla_3']], placeholder='País'),
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
    Output('pessoa_fisica_vs_lojas', 'figure'),
    Input('melhores_clientes_produto', 'value'),
    Input('melhores_clientes_cartao', 'value'),
    Input('melhores_clientes_data_pedido', 'value'),
    Input('melhores_clientes_motivo_venda', 'value'),
    Input('melhores_clientes_cidade', 'value'),
    Input('melhores_clientes_nome_estado', 'value'),
    Input('melhores_clientes_sigla_3', 'value')
)
def render_pedidos_pessoa_fisica_vs_lojas(produto, tipo_cartao, data, motivo_venda, cidade, estado, pais):
    datavisService = DatavisService()
    datavisService.get_data(clientes_vs_lojas_total_negociado_por_dimensao(
            produto, 
            tipo_cartao, 
            motivo_venda,
            data, 
            cidade, 
            estado, 
            pais))
    return datavisService.make_bar_graph(
        x='cliente', 
        y='total', 
        title='Pessoa Física vs Lojas',
        style_dict=colors)

@callback(
    Output('melhores_clientes', 'figure'),
    Input('melhores_clientes_produto', 'value'),
    Input('melhores_clientes_cartao', 'value'),
    Input('melhores_clientes_data_pedido', 'value'),
    Input('melhores_clientes_motivo_venda', 'value'),
    Input('melhores_clientes_cidade', 'value'),
    Input('melhores_clientes_nome_estado', 'value'),
    Input('melhores_clientes_sigla_3', 'value')
)
def render_clientes(produto, tipo_cartao, data, motivo_venda, cidade, estado, pais):
    datavisService = DatavisService()
    datavisService.get_data(melhores_clientes_total_negociado_por_dimensao(
            produto, 
            tipo_cartao, 
            motivo_venda,
            data, 
            cidade, 
            estado, 
            pais))
    return datavisService.make_bar_graph(
        x='total', 
        y='nome_cliente', 
        title='Melhores clientes - Pessoa Física (total negociado)',
        style_dict=colors,
        orientation='h')       

@callback(
    Output('melhores_lojas', 'figure'),
    Input('melhores_clientes_produto', 'value'),
    Input('melhores_clientes_cartao', 'value'),
    Input('melhores_clientes_data_pedido', 'value'),
    Input('melhores_clientes_motivo_venda', 'value'),
    Input('melhores_clientes_cidade', 'value'),
    Input('melhores_clientes_nome_estado', 'value'),
    Input('melhores_clientes_sigla_3', 'value')
)
def render_lojas(produto, tipo_cartao, data, motivo_venda, cidade, estado, pais):
    datavisService = DatavisService()
    datavisService.get_data(melhores_lojas_total_negociado_por_dimensao(
            produto, 
            tipo_cartao, 
            motivo_venda,
            data, 
            cidade, 
            estado, 
            pais))
    return datavisService.make_bar_graph(
        x='total', 
        y='nome_loja', 
        title='Melhores clientes - Lojas (total negociado)',
        style_dict=colors,
        orientation='h')  