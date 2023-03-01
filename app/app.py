from dash import Dash, html
from utils import quantidade_comprada_por_pais, total_pedido_por_pais, \
                    count_query_pais, dimensoes_categorias, colors, DIMENSOES

from components import PedidosAgregadosGraph, QuantidadeCompradaAgregadosGraph, \
                        TotalNegociadoAgregadosGraph, MapaMundiMetricasGraph, PedidosTemporalGraph, \
                        TicketMedioAgregadosGraph, MetricasTotaisFiltrados, MelhoresClientesGraph, \
                        ProdutosVendidosEmPromo, QuantidadeTemporalGraph, TotalNegociadoTemporalGraph


app = Dash('cea-aw-johann')

dimensoes_dict = dimensoes_categorias()

def updated_layout():
    layout = html.Div(children=[
        html.H1(children='ACADEMY  DBT  JOHANN', style={'color': colors['dark-bg-txt']}),
        html.Div([
            html.Div(children=[
                MetricasTotaisFiltrados(dimensoes_dict)
            ],
            style={'display': 'flex'}),
            
            html.Div([
                TicketMedioAgregadosGraph()
            ],
            style={'display': 'flex'}),

            html.Div([
                MelhoresClientesGraph(dimensoes_dict)
            ],
            style={'display': 'flex'}),
            
            html.Div(children=[
                PedidosAgregadosGraph(DIMENSOES),
                MapaMundiMetricasGraph('Número de pedidos por país', count_query_pais())
            ],
            style={'display': 'flex'}),

            html.Div([
                QuantidadeCompradaAgregadosGraph(DIMENSOES),
                MapaMundiMetricasGraph('Quantidade comprada por país', quantidade_comprada_por_pais())

            ],
            style={'display': 'flex'}),

            html.Div([
                TotalNegociadoAgregadosGraph(DIMENSOES),
                MapaMundiMetricasGraph('Total negociado por país', total_pedido_por_pais()),
            ],
            style={'display': 'flex'}),

            html.Div([
                PedidosTemporalGraph()
            ],
            style={'display': 'flex'}),
            
            html.Div([
                QuantidadeTemporalGraph()
            ],
            style={'display': 'flex'}),
            
            html.Div([
                TotalNegociadoTemporalGraph()
            ],
            style={'display': 'flex'}),
            
            html.Div([
                ProdutosVendidosEmPromo()
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