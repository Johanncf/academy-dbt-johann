from dash import dcc, html
from utils import colors
from typing import List

def Dropdown(id: str, options: List[dict], placeholder: str = 'Selecione uma dimensão'):
    return html.Div(
        dcc.Dropdown(
            id=id,
            placeholder=placeholder,
            options=[
                {
                    'label': html.Span([option['name']], style={'color': colors['dark-bg-txt'], 'font-size': 15}),
                    'value': option['value'],
                } 
                for option in options
            ]
        ),
        style={'width': '100%'})