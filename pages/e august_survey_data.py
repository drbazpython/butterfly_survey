import dash
from dash import html

dash.register_page(__name__,path='/August',name="August Survey Data")

layout = html.Div([
    html.Br(),
    html.H2('August Survey Data - Under Construction'),
    #html.Div('This is our Archive page content.'),
])
