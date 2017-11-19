# coding=UTF-8
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly import graph_objs as go
from plotly.graph_objs import *
import dataAnalyzer

dataAnalyzer = dataAnalyzer.DataAnalyzer()

app = dash.Dash()

mapbox_access_token = 'pk.eyJ1IjoiYWxpc2hvYmVpcmkiLCJhIjoiY2ozYnM3YTUxMDAxeDMzcGNjbmZyMmplZiJ9.ZjmQ0C2MNs1AzEBC_Syadg'

app.layout = html.Div(children=[

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dcc.Graph(
        id='map-graph',
        figure={
            'data': [
                Scattermapbox(
                    lat=dataAnalyzer.get_allBikePostsLatitude(),
                    lon=dataAnalyzer.get_allBikePostsLongitude(),
                    mode='markers',
                    marker=Marker(
                        size=12,
                        color='rgb(255, 0, 0)',
                        opacity=0.7
                    ),
                    text=dataAnalyzer.get_allBikePostsName(),
                )
            ],
            'layout': go.Layout(autosize=True,
                                height=750,
                                margin=Margin(l=0, r=0, t=0, b=0),
                                showlegend=False,
                                mapbox=dict(
                                    accesstoken=mapbox_access_token,
                                    center=dict(
                                        lat=40.7272,
                                        lon=-73.991251
                                    ),
                                    style='dark',
                                    bearing=0,
                                    zoom=12.0
                                ))
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
