from dash import dcc, html
from .Dropdown import Dropdown
from typing import List

def GraphWithDropdownFilter(graph_id: str, dropdown_id: str, options: List[dict]):
    return html.Div(children=[
        dcc.Graph(id=graph_id),
        html.Div(
            Dropdown(dropdown_id, options),
            style={'width': '100%', 'marginTop': '20px'}
        )
    ],
    style={'backgroundColor': 'black', 'marginTop': '100px', 'width': '50%'})