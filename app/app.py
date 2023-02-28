from dash import Dash, html
from services import DatavisService
from utils import quantidade_comprada_por_pais, total_pedido_por_pais, count_query_pais
from components import PedidosAgregadosGraph, QuantidadeCompradaAgregadosGraph, \
                        TotalNegociadoAgregadosGraph, MapaMundiMetricasGraph, PedidosTemporalGraph, \
                        TicketMedioAgregadosGraph, MetricasTotaisFiltrados, MelhoresClientesGraph


app = Dash('cea-aw-johann')

colors = {
    'dark-bg-0': '#000000',
    'dark-bg': '#222222',
    'dark-bg-txt': '#DCDCDC'
}

datavisService = DatavisService()

DIMENSOES_1 = [
    {
        'name': 'produto',
        'value': 'nome_produto'
    },
    {
        'name': 'cliente',
        'value': 'nome_cliente'
    },
    {
        'name': 'tipo do cartão',
        'value': 'tipo_cartao'
    },
    {
        'name': 'motivador da compra',
        'value': 'motivo_venda'
    },
    {
        'name': 'status do pedido',
        'value': 'status_pedido'
    },
    {
        'name': 'cidade',
        'value': 'cidade'
    },
    {
        'name': 'estado',
        'value': 'nome_estado'
    }
]

def updated_layout():
    layout = html.Div(children=[
        html.H1(children='ACADEMY DBT JOHANN'),
        html.Div([
            html.Div(children=[
                MetricasTotaisFiltrados()
            ],
            style={'display': 'flex'}),
            
            html.Div([
                TicketMedioAgregadosGraph()
            ],
            style={'display': 'flex'}),

            html.Div([
                MelhoresClientesGraph()
            ],
            style={'display': 'flex'}),
            
            html.Div(children=[
                PedidosAgregadosGraph(DIMENSOES_1),
                MapaMundiMetricasGraph('Número de pedidos por país', count_query_pais())
            ],
            style={'display': 'flex'}),

            html.Div([
                QuantidadeCompradaAgregadosGraph(DIMENSOES_1),
                MapaMundiMetricasGraph('Quantidade comprada por país', quantidade_comprada_por_pais())

            ],
            style={'display': 'flex'}),

            html.Div([
                TotalNegociadoAgregadosGraph(DIMENSOES_1),
                MapaMundiMetricasGraph('Total negociado por país', total_pedido_por_pais()),
            ],
            style={'display': 'flex'}),

            html.Div([
                PedidosTemporalGraph()
            ],
            style={'display': 'flex'})
        ],
        style={
            'display': 'flex',
            'flex-direction': 'column',
            'gap': '5%',
            'width': '100%'
        })
    ],
    style={
        'background-color': colors['dark-bg'], 
        'color': colors['dark-bg-txt'], 
        'textAlign': 'center',
        'padding': '4%',
        'height': '100%'
    })
    return layout

app.layout = updated_layout

if __name__ == '__main__':
    app.run_server()