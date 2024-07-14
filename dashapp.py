import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import numpy as np
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

load_figure_template("darkly")


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY],
    suppress_callback_exceptions=True,
    requests_pathname_prefix="/dashboard1/",
)


app.layout = [
    html.H1(children="Title of Dash App", style={"textAlign": "center"}),
    dcc.Graph(
        id="live-update-graph",
        responsive=True,
        style={"height": "90vh"},
    ),
    dcc.Interval(
        id="interval-component",
        interval=1 * 1000,  # in milliseconds
        n_intervals=0,
    ),
]


@callback(
    Output("live-update-graph", "figure"), Input("interval-component", "n_intervals")
)
def update_graph(n):
    df = pd.DataFrame(dict(x=[1, 3, 2, 4], y=[1, 2, 3, 4]))

    new_df = pd.DataFrame(
        {
            "x": n,
            "y": np.random.randint(1, 20, size=1),
        }
    )

    df = pd.concat([df, new_df], ignore_index=True)

    return px.line(df, x="x", y="y", title="Graph Title", template="darkly")


if __name__ == "__main__":
    app.run(debug=True)
