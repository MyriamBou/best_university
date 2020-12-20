#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:05:53 2020

@author: randon
"""

import dash_table
import pandas as pd

import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px


df = pd.read_csv('timesData.csv')
df2 = df
#fig = px.scatter(df, x='income', y='international', color='year', title='International score in terms of the income score per year' )

colors = {
    'background': '#111111',
    'text': '#ffffff'
}

#fig.update_layout(
    #plot_bgcolor=colors['background'],
    #paper_bgcolor=colors['background'],
    #font_color=colors['text'])

layout = html.Div(children=[
    html.Div(children=[
        html.H1(
            children='Explorez les données des 50 meilleurs universités en 2016',
            style={
                'textAlign': 'center',
                }
            )
        ]),
  
        
    html.Div([
        dash_table.DataTable(
            data=df2.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df2.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'height': 'auto',
                'width': 'auto',
                'whiteSpace': 'normal',
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white'
                }
            )
        ]),
    html.Div(style={'color': 'white'}, children=[
        html.H1(
            children='',
            style={
                'textAlign': 'center',
                'color': colors['text']
                }
            )
        ]),

    #html.Div(style={'backgroundColor': colors['background']}, 
             #children=html.Div(
             #'Graphique',
         #style={
        #'textAlign': 'center',
        #'color': colors['text']
    #})
        #),

    #dcc.Graph(
       # id='example-graph-2',
        #figure=fig
       # )
    ])
