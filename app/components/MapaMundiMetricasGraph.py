from dash import dcc, html
from services import DatavisService
from utils import colors

def MapaMundiMetricasGraph(title: str, query: str):
    QUERY = (
        f'''
        SELECT COUNT(*) total, sigla_3 pais
        FROM `dbt_adventure_works.vendas` 
        GROUP BY `sigla_3`
        ORDER BY total DESC
        ''')
    datavisService = DatavisService()
    datavisService.get_data(query)
    figure = datavisService.make_map_graph(title, colors)
    
    return html.Div(children=[
        dcc.Graph(figure=figure)
    ],
    style={'width': '50%', 'marginTop': '100px'})