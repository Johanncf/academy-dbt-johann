from dash import dcc, html
from services import DatavisService
from utils import total_negociado_serie_temporal, colors

def TotalNegociadoTemporalGraph():
    datavisService = DatavisService()
    datavisService.get_data(total_negociado_serie_temporal())
    figure = datavisService.make_time_serie_graph('Total negociado - Análise temporal', colors)
    
    return html.Div(children=[
        dcc.Graph(figure=figure, id='total_temporal')
    ], 
    style={'width': '100%', 'height': '100%', 'marginTop': '100px'})