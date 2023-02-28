from dash import dcc, html, callback, Input, Output
from .Dropdown import Dropdown
from services import DatavisService
from utils import numero_pedidos_por_dimensao, write_title, colors
from typing import List

def PedidosAgregadosGraph(options: List[dict]):
    return html.Div(children=[
        dcc.Graph(id='pedidos_agregados'),
        html.Div(
            Dropdown('pedidos_agregados_dimensao', options),
            style={'width': '100%'}
        )
    ],
    style={'marginTop': '100px', 'width': '50%'})


@callback(
    Output('pedidos_agregados', 'figure'),
    Input('pedidos_agregados_dimensao', 'value'),
    Input('pedidos_agregados_dimensao', 'options')
)
def render_graph(value, options):
    datavisService = DatavisService()
    if value is None:
        datavisService.get_data(numero_pedidos_por_dimensao('nome_produto'))
        return datavisService.make_bar_graph(
            x='total', 
            y='nome_produto', 
            title='Número de pedidos por produto', 
            style_dict=colors, 
            orientation='h')

    datavisService.get_data(numero_pedidos_por_dimensao(value))
    title = write_title(value, options)
    return datavisService.make_bar_graph(
        x='total', 
        y=value, 
        title=f'Número de pedidos por {title}',
        style_dict=colors, 
        orientation='h')