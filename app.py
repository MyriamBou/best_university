import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

names = data2016['university_name']
features = data2016_pca.columns

fig = px.scatter_matrix(
    data2016,
    dimensions=features,
    color="num_students"
)
fig.update_traces(diagonal_visible=False)
fig.show()






app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} 
                 for x in all_dims],
        value=all_dims[:2],
        multi=True
    ),
    dcc.Graph(id="splom"),
])


@app.callback(
    Output("splom", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(dims):
    fig = px.scatter_matrix(
        data2016, dimensions=dims, color="species")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
