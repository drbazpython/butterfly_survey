# brown hairstreak
# small copper

import dash
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
from dash import Input, Output, callback,html, dcc

local = True
# Initialize the app
app = dash.register_page(__name__,path='/May',name="May Survey Data")
if local:
    df = pd.read_excel('may_butterflies.xlsx').fillna(0)
else:
    df = pd.read_excel('/home/drbaz/butterfly_survey/may_butterflies.xlsx').fillna(0)
#print(df)
surveyor = df.iat[0,1]
#print(df.iat[0,2], df.iat[0,3],df.iat[0,4],df.iat[0,5],df.iat[0,6])
#survey_date = df.iat[0,6].strftime('%d %b %Y') # needs formatimg
survey_date = df.iat[0,6].strftime('%b %Y')
survey_start_time = df.iat[1,1].strftime('%H:%M')
survey_end_time = df.iat[1,6].strftime('%H:%M')
sunshine = df.iat[2,1]
temperature = df.iat[2,6]
#transect = df.iat[4,1]
print(surveyor, survey_date, survey_start_time, survey_end_time, sunshine, temperature)
df = df.drop([0,1,2,3,4,5,6],axis=0)
df1 = df.iloc(axis=1)[0:5]
df2 = df.iloc(axis=1)[[0,5,6,7,8]]
df3 = df.iloc(axis=1)[[0,9,10,11,12]]
df_totals = df.iloc(axis=1)[[0,13]]
df.columns = ["name","1-A","1-B","1-C","1-total","2-A","2-B","2-C","2-total","3-A","3-B","3-C","3-total","total"]  # noqa: E501

df1.columns = ["name","1-A","1-B","1-C","1-total"]
df2.columns = ["name","2-A","2-B","2-C","2-total"]
df3.columns = ["name","3-A","3-B","3-C","3-total"]
df_totals.columns = ["name","total"]
#print(df1)
#print(df2)

layout = html.Div([
    html.Br(),
    html.Div(className='row1', children='Butterfly Survey for Transects 1,2 and 3 - Test Data',  # noqa: E501
             style={'textAlign': 'center', 'color': 'red', 'fontSize': 30}),
    html.Br(),
    # html.Div(className='row2', children=f'Surveyor: {surveyor} Surveys for  {survey_date} between {survey_start_time} and {survey_end_time}',  # noqa: E501
    #          style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}),
    html.Div(className='row2', children=f'Surveys for  {survey_date}',
            style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}),

    # html.Div(className='row3', children=f'Sunshine: {sunshine}% Temperature:{temperature}degC',  # noqa: E501
    #          style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}),
    html.Br(),

    html.Div(className='row', children=[
        html.Div(className='eight columns', children=[
            dag.AgGrid(
                className='ag-theme-alpine',
                id="grid",
                rowData=df.to_dict('records'),
                columnDefs=[{"field":i} for i in df.columns],
                dashGridOptions={"rowSelection":"single",},
                #selectedRows=df[0],
                style={'display': 'inline-block'}
            )
            ]),

        html.Div(className="row", children=[
            html.Img(id="butterfly_image",src="/static/no_image.jpg",
                     style={'display': 'inline-block',"width":"25%"}),
            #html.Img(id="butterfly_image",src="/assets/no_image.jpg",
                     #style={'display': 'inline-block',"width":"25%"}),
            html.Br(),
            html.A(id="butterfly_url",children=["More Info"],style={"marginLeft":50}, href="https://butterfly-conservation.org/butterflies/identify-a-butterfly")
        ],style={'marginLeft':50}),
    ]),
        html.Br(),
        html.Br(),
    html.Div(className='row', children=[
        html.Div(className='twelve columns', children=[
            dcc.RadioItems(options=['1-total', '1-A', '1-B','1-C'],
                       value='1-total',
                       inline=True,
                       id='my-radio-buttons-final1'),
            dcc.Graph(figure={}, id='histo-chart-final1'),

        ]),
    ]),
    html.Div(className='row', children=[
            html.Div(className='twelve columns', children=[
            dcc.RadioItems(options=['2-total', '2-A', '2-B','2-C'],
                       value='2-total',
                       inline=True,
                       id='my-radio-buttons-final2'),
            dcc.Graph(figure={}, id='histo-chart-final2'),
        ]),
    ]),
    html.Div(className='row', children=[
        html.Div(className='twelve columns', children=[
            dcc.RadioItems(options=['3-total', '3-A', '3-B','3-C'],
                       value='3-total',
                       inline=True,
                       id='my-radio-buttons-final3'),
            dcc.Graph(figure={}, id='histo-chart-final3'),
        ]),
    ]
    ,style={
    'textAlign': 'center',
    "margin-left":"20px",
    "margin-right":"20px",
    "width":"90%",
                        }),

    html.Div(className='row', children=[
        html.Div(className='twelve columns', children=[
            dcc.RadioItems(options=['total', '3-total', '2-total','1-total'],
                       value='total',
                       inline=True,
                       id='my-radio-buttons-final4'),
            html.Label("Totals"),
            dcc.Graph(figure={}, id='histo-chart-final4'),
        ]),
    ])
])

# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart-final1', component_property='figure'),
    Output(component_id='histo-chart-final2', component_property='figure'),
    Output(component_id='histo-chart-final3', component_property='figure'),
    Output(component_id='histo-chart-final4', component_property='figure'),
    Output(component_id='butterfly_image', component_property='src'),
    Output(component_id='butterfly_url', component_property='href'),
    Input(component_id='my-radio-buttons-final1', component_property='value'),
    Input(component_id='my-radio-buttons-final2', component_property='value'),
    Input(component_id='my-radio-buttons-final3', component_property='value'),
    Input(component_id='my-radio-buttons-final4', component_property='value'),
    Input(component_id='grid', component_property="selectedRows")
)
def update_graph(col_chosen1,col_chosen2, col_chosen3,col_chosen4, my_row):

    butterfly_src = "/home/drbaz/butterfly_survey/assets/no_image.jpg"
    butterfly_url = "https://butterfly-conservation.org/butterflies/identify-a-butterfly"
    if my_row:
        butterfly_name = my_row[0]["name"].lower()
        # prepare src for image eg assets/{butterfly_name}.jpg
        #butterfly_src = f"/home/drbaz/butterfly_survey/assets/{butterfly_name}.jpg"
        if local:
            butterfly_src=f"/assets/{butterfly_name}.jpg"
        else:
            butterfly_src=f"/static/{butterfly_name}.jpg"
        butterfly_url_name = butterfly_name.replace(" ","-")
        butterfly_url = f"https://butterfly-conservation.org/butterflies/{butterfly_url_name}"
        print(f"Butterfly src: {butterfly_src}")
        # if no image, use "no_image.jpg"
        #if not os.path.exists(f"/static/{butterfly_name}.jpg"):
          #  print(f"BUTTERFLY_SRC = {butterfly_src}")
           # print("does not exist")
            #butterfly_src = "/home/drbaz/butterfly_survey/assets/no_image.jpg"

    #print(f"URL: {butterfly_url}")
    fig1 = px.bar(df1,x='name', y=col_chosen1,labels={"name":"Butterfly Name"})
    fig2 = px.bar(df2,x='name', y=col_chosen2,labels={"name":"Butterfly Name"})
    fig3 = px.bar(df3,x='name', y=col_chosen3,labels={"name":"Butterfly Name"})
    fig4 = px.bar(df,x='name', y=col_chosen4,labels={"name":"Butterfly Name"})
    return fig1,fig2,fig3, fig4, butterfly_src, butterfly_url

# Run the app
if __name__ == '__main__':
    app.run(debug=True,port=5500)
