from dash import html
from utils import colors

def MetricasCard(title: str, id:str):
    return html.Div([
        html.H3(title),
        html.Div(id=id, style={'font-size': 'xxx-large'})
    ], style={
        'backgroundColor': colors['dark-bg'],
        'width': '25%',
        'height': '200px',
        'margin': '20px',
        'display': 'flex',
        'flexDirection': 'column',
        'gap': '20px',
    })