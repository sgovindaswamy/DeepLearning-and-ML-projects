# -*- coding: utf-8 -*-
"""
This is a script for creating Dash web application

"""

import pandas as pd
import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px


""" Working module """

df = pd.read_csv('ai4i2020.csv')

# Create Dash application
app = dash.Dash(__name__)

# Define the layout of the web app
app.layout = html.Div([
    html.H1("Interactive visualization of Ai4i 2020 (synthetic predictive maintenance dataset)"),
    
    # Dropdown for selecting a variable for the x-axis
    dcc.Dropdown(
        id='x-axis-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[0],
        clearable=False
    ),
    
    # Dropdown for selecting a variable for the y-axis
    dcc.Dropdown(
        id='y-axis-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[1],
        clearable=False
    ),
    
    # Graph for displaying the scatter plot
    dcc.Graph(id='scatter-plot')
])

# Define callback to update graph dynamically
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value')]
)
def update_graph(x_col, y_col):
    # Generate plot using Plotly Express
    fig = px.scatter(df, x=x_col, y=y_col, title=f'Scatter plot of {x_col} vs {y_col}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(host='192.168.1.80', port=8050, debug=True)

""" 
Host address is your local IP address. you can identify by typing 'ipconfig' in your 
command prompt and replace the existing address with your Local IP address

"""

