from dash import dcc, html, callback, Input, Output
from .Dropdown import Dropdown
from .GraphWithDropdownFilter import GraphWithDropdownFilter
from services import DatavisService
from utils import quantidade_comprada_serie_temporal, write_title, colors
from typing import List

def PedidosTemporalGraph():
    datavisService = DatavisService()
    datavisService.get_data(quantidade_comprada_serie_temporal())
    figure = datavisService.make_time_serie_graph('Número de pedidos - Análise temporal', colors)
    return html.Div(children=[
        dcc.Graph(figure=figure, id='pedidos_temporal')
    ], 
    style={'width': '100%', 'height': '100%', 'marginTop': '100px'})