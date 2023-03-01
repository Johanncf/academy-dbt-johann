from dash import dcc, html
from services import DatavisService
from utils import numero_pedidos_serie_temporal, colors

def PedidosTemporalGraph():
    datavisService = DatavisService()
    datavisService.get_data(numero_pedidos_serie_temporal())
    figure = datavisService.make_time_serie_graph('Número de pedidos - Análise temporal', colors)
    
    return html.Div(children=[
        dcc.Graph(figure=figure, id='pedidos_temporal')
    ], 
    style={'width': '100%', 'height': '100%', 'marginTop': '100px'})