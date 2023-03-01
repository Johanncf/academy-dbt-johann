from datetime import datetime
import json
import pandas as pd
import plotly.express as px
from pandas import DataFrame
from datetime import datetime
from google.cloud import bigquery
from google.oauth2 import service_account


class DatavisService():
    def __init__(self):
        self.data: DataFrame 

        credentials = service_account.Credentials.from_service_account_file(
            r"cea-adw-johann.json")
        self.client: bigquery.Client = bigquery.Client(credentials=credentials)

    def get_data(self, query: str):
        query_job = self.client.query(query)
        self.data = query_job.to_dataframe()
        return self.data

    def make_bar_graph(self, x: str, y: str, title: str, style_dict: dict, orientation='v'):
        #self.get_data(y)
        fig = px.bar(
            self.data[:15], 
            x=x, 
            y=y,
            title=title,
            labels={'index': x, 'value': y, 'color': x}, orientation=orientation)
        fig.update_layout(
            plot_bgcolor=style_dict['dark-bg-0'],
            paper_bgcolor=style_dict['dark-bg-0'],
            font_color=style_dict['dark-bg-txt'],
            barmode='stack', 
            yaxis={'categoryorder':'total ascending'}
        )

        return fig

    def make_map_graph(self, title:str, style_dict: dict):
        fig = px.choropleth(
            self.data, 
            title=title,
            locations='pais', 
            locationmode='ISO-3', 
            color='total')
        fig.update_layout(
            plot_bgcolor=style_dict['dark-bg-0'],
            paper_bgcolor=style_dict['dark-bg-0'],
            font_color=style_dict['dark-bg-txt'],
            geo=dict(bgcolor=style_dict['dark-bg'])
        )
        return fig

    def make_time_serie_graph(self, title: str, style_dict: dict):
        fig = px.area(
            self.data, 
            x='data', 
            y='total', 
            title=title)
        fig.update_layout(
            {'xaxis': {'nticks': 10, 'tick0': 100}},
            plot_bgcolor=style_dict['dark-bg-0'],
            paper_bgcolor=style_dict['dark-bg-0'],
            font_color=style_dict['dark-bg-txt'],
        )
        fig.update_xaxes(showgrid=False)
        return fig
      