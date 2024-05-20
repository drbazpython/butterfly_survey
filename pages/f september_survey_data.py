import dash
from dash import html

dash.register_page(__name__,path='/September',name="September Survey Data")

layout = html.Div([
    html.Br(),
    html.H2('September Survey Data - Under Construction'),
    #html.Div('This is our Archive page content.'),
])
