from dash import dcc, html
from services import DatavisService
from utils import quantidade_comprada_serie_temporal, colors

def QuantidadeTemporalGraph():
    datavisService = DatavisService()
    datavisService.get_data(quantidade_comprada_serie_temporal())
    figure = datavisService.make_time_serie_graph('Quantidade comprada - Análise temporal', colors)
    
    return html.Div(children=[
        dcc.Graph(figure=figure, id='quantidade_temporal')
    ], 
    style={'width': '100%', 'height': '100%', 'marginTop': '100px'})