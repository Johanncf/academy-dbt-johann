from dash import callback, Input, Output
from .GraphWithDropdownFilter import GraphWithDropdownFilter
from services import DatavisService
from utils import numero_pedidos_por_dimensao, write_title, colors
from typing import List

def PedidosAgregadosGraph(options: List[dict]):
    return GraphWithDropdownFilter(
        graph_id='pedidos_agregados',
        dropdown_id='pedidos_agregados_dimensao',
        options=options)


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