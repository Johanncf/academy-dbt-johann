from dash import dcc, html, callback, Input, Output
from .Dropdown import Dropdown
from .GraphWithDropdownFilter import GraphWithDropdownFilter
from services import DatavisService
from utils import total_negociado_por_dimensao, write_title, colors
from typing import List

def TotalNegociadoAgregadosGraph(options: List[dict]):
    return GraphWithDropdownFilter(
        graph_id='total_negociado_agregados',
        dropdown_id='total_negociado_agregados_dimensao',
        options=options)
    
    # html.Div(children=[
    #     html.Div(
    #         Dropdown('total_negociado_agregados_dimensao', options),
    #         style={'width': '50%'}
    #     ),
    #     dcc.Graph(id='total_negociado_agregados')
    # ],
    # style={'marginTop': '100px', 'width': '50%'})


@callback(
    Output('total_negociado_agregados', 'figure'),
    Input('total_negociado_agregados_dimensao', 'value'),
    Input('total_negociado_agregados_dimensao', 'options')
)
def render_graph(value, options):
    datavisService = DatavisService()
    if value is None:
        datavisService.get_data(total_negociado_por_dimensao('nome_produto'))
        return datavisService.make_bar_graph(
            x='total', 
            y='nome_produto', 
            title='Total negociado por produto', 
            style_dict=colors, 
            orientation='h')

    datavisService.get_data(total_negociado_por_dimensao(value))
    title = write_title(value, options)
    return datavisService.make_bar_graph(
        x='total', 
        y=value, 
        title=f'Total negociado por {title}',
        style_dict=colors, 
        orientation='h')