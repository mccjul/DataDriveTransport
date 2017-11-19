# coding=UTF-8
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly import graph_objs as go
from plotly.graph_objs import *
import util
import dataparser

app = dash.Dash()

lat = 40.7272
lon = -73.991251
zoom = 12.0

rangemap = {
    'N': 40.758924,
    'S': 40.679543,
    'W': -74.047536,
    'E': -73.888193
}
dataparser = dataparser.Dataparser(rangemap)

mapbox_access_token = 'pk.eyJ1IjoiYWxpc2hvYmVpcmkiLCJhIjoiY2ozYnM3YTUxMDAxeDMzcGNjbmZyMmplZiJ9.ZjmQ0C2MNs1AzEBC_Syadg'

data = [
    Scattermapbox(
        lat=dataparser.get_allBikePostsLatitudeList(),
        lon=dataparser.get_allBikePostsLongitudeList(),
        mode='markers',
        marker=Marker(
            size=8,
            color='rgb(255, 0, 0)',
            opacity=0.7
        ),
        text=dataparser.get_allBikePostsNameList(),
    )
]

app.layout = html.Div(children=[
    html.Div([
        html.Div(
            [
                dcc.Graph(
                    id='map-graph',
                    figure={
                        'data': data,
                        'layout': go.Layout(
                            autosize=True,
                            height=600,
                            width=900,
                            margin=dict(l=0, r=0, b=0, t=0),
                            showlegend=False,
                            hovermode='closest',
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
                        'data': [{
                            "values": [16, 15, 12, 6, 5, 4, 42],
                            "labels": [
                                "US",
                                "China",
                                "European Union",
                                "Russian Federation",
                                "Brazil",
                                "India",
                                "Rest of World"
                            ],
                            "domain": {'x': [.5, 1],
                                       'y': [.51, 1]},
                            "name": "GHG Emissions",
                            "hoverinfo": "label+percent+name",
                            "type": "pie"
                        }],
                        'layout': {
                            'title': 'Chart 1',
                            'margin': dict(
                                l=0,
                                r=0,
                                b=0,
                                t=30),
                            'height': 295
                        }
                    }
                ),
                dcc.Graph(
                    id='example-graph2',
                    figure={
                        'data': [
                            {'x': dataparser.get_mostPopularCustomerPathList(5),
                             'y': dataparser.get_mostPopularCustomerPathCountList(5),
                             'type': 'bar',
                             'name': 'Customer'
                             },
                            {'x': dataparser.get_mostPopularSubscriberPathList(5),
                             'y': dataparser.get_mostPopularSubscriberPathCountList(5),
                             'type': 'bar',
                             'name': 'Subscriber'
                             },
                        ],
                        'layout': {
                            'title': 'Chart 2',
                            'margin': dict(
                                l=0,
                                r=0,
                                b=0,
                                t=40),
                            'height': 295
                        }
                    }
                )
            ],
            className='four columns', style={'margin-top': '10', 'height': 500}
        )
    ], className='row'),
    html.Div([
        dcc.Slider(
            id="month-slider",
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) for i in range(10)},
            value=0,
        )
    ], style={'margin-left': 20, 'margin-right': 20, 'margin-top': 40})
])


@app.callback(Output('map-graph', 'figure'), [Input('month-slider', 'value')], [State('month-slider', 'value')])
def updateMapPerMonth(trigger, value):
    print(value)
    return {
        'data': data,
        'layout': go.Layout(
            autosize=True,
            height=600,
            width=900,
            margin=dict(l=0, r=0, b=0, t=0),
            showlegend=False,
            hovermode='closest',
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


@app.callback(Output('example-graph1', 'figure'), [], [State('map-graph', 'relayoutData')],
              [Event('map-graph', 'relayout')])
def updateGraph1OnMapMove(relayoutData):
    res = boundBox(relayoutData)
    print(res)
    return {
        'data': [{
            "values": [16, 15, 12, 6, 5, 4, 42],
            "labels": [
                "US",
                "China",
                "European Union",
                "Russian Federation",
                "Brazil",
                "India",
                "Rest of World"
            ],
            "domain": {'x': [.5, 1],
                       'y': [.51, 1]},
            "name": "GHG Emissions",
            "hoverinfo": "label+percent+name",
            "type": "pie"
        }],
        'layout': {
            'title': 'Chart 1',
            'margin': dict(
                l=0,
                r=0,
                b=0,
                t=30),
            'height': 295
        }
    }


@app.callback(Output('example-graph2', 'figure'), [], [State('map-graph', 'relayoutData')],
              [Event('map-graph', 'relayout')])
def updateGraph2OnMapMove(relayoutData):
    res = boundBox(relayoutData)
    dataparser.set_dfRangeBikepost(res)
    print(res)

    return {
        'data': [
            {'x': dataparser.get_mostPopularCustomerPathList(5),
             'y': dataparser.get_mostPopularCustomerPathCountList(5),
             'type': 'bar',
             'name': 'Customer'
             },
            {'x': dataparser.get_mostPopularSubscriberPathList(5),
             'y': dataparser.get_mostPopularSubscriberPathCountList(5),
             'type': 'bar',
             'name': 'Subscriber'
             },
        ],
        'layout': {
            'title': 'Chart 2',
            'height': '300',
            'margin': dict(l=0, r=0, b=0, t=100)
        }
    }


def boundBox(relayout):
    # Updating globals at the same time so we can hack the event portion of callbacks
    lon = float(relayout['mapbox']['center']['lon'])
    lat = float(relayout['mapbox']['center']['lat'])
    zoom = float(relayout['mapbox']['zoom'])
    return util.getCorners({'lat': lat, 'lng': lon}, zoom, 900, 500)


app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=True)
