# coding=UTF-8
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly import graph_objs as go
from plotly.graph_objs import *
import util

app = dash.Dash()

lat=40.7272
lon=-73.991251
zoom = 12.0

mapbox_access_token = 'pk.eyJ1IjoiYWxpc2hvYmVpcmkiLCJhIjoiY2ozYnM3YTUxMDAxeDMzcGNjbmZyMmplZiJ9.ZjmQ0C2MNs1AzEBC_Syadg'

app.layout = html.Div(children=[
    html.Div([
        html.Div(
            [
                dcc.Graph(
                    id='map-graph',
                    figure={
                        'data': [
                            Scattermapbox(
                                lat=['40.7272', '40.6945', '40.7272'],
                                lon=['-73.991251', '-73.991251', '-73.911200'],

                                marker=Marker(
                                    size=14
                                ),
                                text=['Montreal', 'Bob town', 'Mary town'],
                                customdata=['thing1', 'thing2', 'thing3']
                            )
                        ],
                        'layout': go.Layout(
                            autosize=True,
                            height=500,
                            width=900,
                            margin=dict(l=0, r=0, b=0, t=0),
                            showlegend=False,
                            hovermode= 'closest',
                            mapbox=dict(
                                accesstoken=mapbox_access_token,
                                center=dict(
                                    lat=lat,
                                    lon=lon
                                ),
                                style='dark',
                                bearing=0,
                                zoom=zoom
                            )

                        )
                    }
                )], className='eight columns'),
        html.Div(
            [
                dcc.Graph(
                    id='example-graph1',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Chart 1',
                            'height': '250',
                            'margin': dict(
                                l=0,
                                r=0,
                                b=0,
                                t=30)
                        }
                    }
                ),
                dcc.Graph(
                    id='example-graph2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Chart 2',
                            'height': '250',
                            'margin': dict(
                                l=0,
                                r=0,
                                b=0,
                                t=40)
                        }
                    }
                )
            ],
            className='four columns', style={'height': '500', 'margin-left': '10'}
        )
    ], className='row'),
    html.Div([
        dcc.Graph(
            id='example-graph3',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
                ],
                'layout': {
                    'title': 'Chart 3',
                    'height': '300',
                    'margin': dict(
                        l=0,
                        r=0,
                        b=0,
                        t=100)
                }
            }
        )
    ])
])

@app.callback(Output('example-graph1', 'figure'), [], [State('map-graph', 'relayoutData')],
              [Event('map-graph', 'relayout')])
def updateGraph1OnMapMove(relayoutData):
    res = boundBox(relayoutData)
    return {
        'data': [
            {'x': [1, 2, 3], 'y': [2, 1, 2], 'type': 'bar', 'name': 'SF'},
        ],
        'layout': {
            'title': 'Chart 1',
            'height': '300',
            'margin': dict(l=0, r=0, b=0, t=100)
        }
    }

@app.callback(Output('example-graph2', 'figure'), [], [State('map-graph', 'relayoutData')],
              [Event('map-graph', 'relayout')])
def updateGraph2OnMapMove(relayoutData):
    res=boundBox(relayoutData)
    return {
        'data': [
            {'x': [1, 2, 3], 'y': [2, 1, 2], 'type': 'bar', 'name': 'SF'},
        ],
        'layout': {
            'title': 'Chart 2',
            'height': '300',
            'margin': dict(l=0, r=0, b=0, t=100)
        }
    }

@app.callback(Output('example-graph3', 'figure'), [], [State('map-graph', 'relayoutData')],
              [Event('map-graph', 'relayout')])
def updateGraph3OnMapMove(relayoutData):
    res = boundBox(relayoutData)
    print(relayoutData)
    print(res)
    return {
        'data': [
            {'x': [1, 2, 3], 'y': [2, 1, 2], 'type': 'bar', 'name': 'SF'},
        ],
        'layout': {
            'title': 'Chart 3',
            'height': '300',
            'margin': dict(l=0, r=0, b=0, t=100)
        }
    }

def boundBox(relayout):
    #Updating globals at the same time so we can hack the event portion of callbacks
    lon = float(relayout['mapbox']['center']['lon'])
    lat = float(relayout['mapbox']['center']['lat'])
    zoom = float(relayout['mapbox']['zoom'])
    return util.getCorners({'lat': lat, 'lng': lon}, zoom,  900, 500)

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=True)
