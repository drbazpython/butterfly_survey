import dash
from dash import html

dash.register_page(__name__,path='/Map',name="Transects Map",)

layout = html.Div( children=[
    html.H1('Butterfly Survey Transects Map'),
    html.Iframe(src="assets/transects.pdf",
                style={"height": "1000px", "width": "100%", })
])
