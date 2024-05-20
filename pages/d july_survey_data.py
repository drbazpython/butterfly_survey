import dash
from dash import html

dash.register_page(__name__,path='/July',name="July Survey Data")

layout = html.Div([
    html.Br(),
    html.H2('July Survey Data - Under Construction'),
    #html.Div('This is our Archive page content.'),
])
