import dash
from dash import html

dash.register_page(__name__,path='/2024',name="Survey Data for 2024")

layout = html.Div([
    html.Br(),
    html.H2('2024 Survey Data - Under Construction'),
    #html.Div('This is our Archive page content.'),
])
