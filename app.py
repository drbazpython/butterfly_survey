# App to show Dash Pages
# Import packages
from dash import Dash, html, page_container, page_registry, dcc

app = Dash(__name__, use_pages=True)
app.config.suppress_callback_exceptions=True

# set up Dash web pages
app.layout = html.Div([
    html.Div([
    html.Img(id="crt_image",src="/assets/crt.png",
                     style={'display': 'inline-block',"width":"5%"}),
    html.H1('Bere Marsh Farm Butterfly Surveys')
    ]),
    html.H4('Please select one of the options below:'),
    html.Div([
        html.Div(
            #dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
            dcc.Link(f"●  {page['name']}", href=page["relative_path"])
        ) for page in page_registry.values()
    ]),
    page_container
])

if __name__ == '__main__':
    app.run(debug=True)
