import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash, dcc, html, Input, Output, callback
from dash.dependencies import Input, Output
import plotly.express as px
dash.register_page(__name__)

df = pd.read_csv("sp_irad_accident.csv")

# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
#app = dash.Dash(__name__)

#---------------------------------------------------------------
layout = html.Div([
    html.Div([
            html.Pre(children= "Pie Charts for RBG Accidents",
            style={"text-align": "center", "font-size":"200%", "color":"black"})
        ]),

    html.Div([
        html.Label(['Choose the Chart you want'],style={"text-align": "center",'font-weight': 'bold'}),
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': 'Crash Types', 'value': 'crash_type'},
                     {'label': 'Year Wise Crashes', 'value': 'year'},
                     {'label': 'Severity Crashes', 'value': 'severity'},
                     {'label': 'Collision Types', 'value': 'collision_type'}
                     
            ],
            value='crash_type',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
    ]),

    html.Div([
        dcc.Graph(id='pie_graph')
    ]),

])

#---------------------------------------------------------------
@callback(
    Output(component_id='pie_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = df

    piechart=px.pie(
            data_frame=dff,
            names=my_dropdown,
            hole=.3,
            )

    return (piechart)


# if __name__ == '__main__':
#     app.run_server(debug=True, port = 3000)

