from dash import dcc, html
from services import DatavisService
from utils import colors, produto_mais_vendido_por_promotion

def ProdutosVendidosEmPromo():
    datavisService = DatavisService()
    datavisService.get_data(produto_mais_vendido_por_promotion())
    figure = datavisService.make_bar_graph(
        x='total',
        y='nome_produto', 
        title='Produtos mais vendidos em promoção',
        style_dict=colors,
        orientation='h')
    
    return html.Div(children=[
        dcc.Graph(figure=figure, id='produtos_promocao')
    ], 
    style={'width': '100%', 'height': '100%', 'marginTop': '100px'})