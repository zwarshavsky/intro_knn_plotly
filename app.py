import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle

########### Initiate the app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.title='knn'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1('Classification of Iris Flower'),
    html.Div([
        html.H6('Sepal Length'),
        dcc.Slider(
            id = 'slide-1',
            min=1,
            max=8,
            step=0.1,
            marks={i:str(i) for i in range(1,9)},
            value=5, 
        
        ),
        html.H6('Petal Length'),
        
        html.H6('# of Neighbors'),
        
        html.H6(id='output-message',children='output will go here'),
        
        
             
             
             ]),
    html.Br(),
    html.A('Code on Github', href='https://github.com/austinlasseter/knn_iris_plotly'),
])

############ Execute the app
if __name__ == '__main__':
    app.run_server()
