from dash import callback, Input, Output
from .GraphWithDropdownFilter import GraphWithDropdownFilter
from services import DatavisService
from utils import quantidade_comprada_por_dimensao, write_title, colors
from typing import List

def QuantidadeCompradaAgregadosGraph(options: List[dict]):
    return GraphWithDropdownFilter(
        graph_id='quantidade_comprada_agregados',
        dropdown_id='quantidade_comprada_dimensoes',
        options=options)

@callback(
    Output('quantidade_comprada_agregados', 'figure'),
    Input('quantidade_comprada_dimensoes', 'value'),
    Input('quantidade_comprada_dimensoes', 'options')
)
def render_graph(value, options):
    datavisService = DatavisService()
    if value is None:
        datavisService.get_data(quantidade_comprada_por_dimensao('nome_produto'))
        return datavisService.make_bar_graph(
            x='total', 
            y='nome_produto', 
            title='Quantidade comprada por produto', 
            style_dict=colors, 
            orientation='h')

    datavisService.get_data(quantidade_comprada_por_dimensao(value))
    title = write_title(value, options)
    return datavisService.make_bar_graph(
        x='total', 
        y=value, 
        title=f'Quantidade comprada por {title}',
        style_dict=colors, 
        orientation='h')