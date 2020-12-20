#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:07:42 2020

@author: randon
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2


app.layout = html.Div([

    
    html.Div(children=[
        html.H1(
            children='Données des 50 meilleurs universités en 2016',
            style={
                'textAlign': 'center',
                }
            )
        ]),
        # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    dcc.Link('Menu principal', href='/'),
    html.Br(),
    dcc.Link('50 meilleurs universités de l année 2016', href='/apps/app1'),
    html.Br(),
    dcc.Link('Résultats issus de l ACP', href='/apps/app2'),
        # content will be rendered in this element
    html.Div(id='page-content'),
    
])


@app.callback(Output('page-content',
              'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)