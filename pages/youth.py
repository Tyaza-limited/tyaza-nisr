import pandas as pd
import dash
from dash import Dash, html, dcc, callback

from dash.dependencies import Input, Output
import plotly.express as px


dash.register_page(__name__)
import kagglehub

path = kagglehub.dataset_download("arshkon/linkedin-job-postings")

print("Path to dataset files:", path)

df = pd.read_csv(path + "/postings.csv")
data = df[["title", "max_salary", "pay_period"]]
df = data.dropna(subset=["title", "max_salary", "pay_period"])


def layout(**kwargs):
    return html.Div(
        [
            html.H1("Job Max Salary Analysis"),
            html.Div(
                [
                    dcc.Dropdown(
                        id="filter-dropdown",
                        options=[
                            {"label": p, "value": p} for p in df["pay_period"].unique()
                        ],
                        value="MONTHLY",
                    ),
                    dcc.Dropdown(
                        id="title-filter",
                        options=[
                            {"label": p, "value": p} for p in df["title"].unique()
                        ],
                        value=df["title"][4],
                    ),
                ]
            ),
            dcc.Graph(id="salary-chart"),
        ]
    )


@callback(
    Output("salary-chart", "figure"),
    Input("filter-dropdown", "value"),
    Input("title-filter", "value"),
)
def update_chart(pay_period_filter, title_filter):
    df_filtered = df.copy()
    if pay_period_filter != "ALL":
        df_filtered = df_filtered[df_filtered["pay_period"] == pay_period_filter]
    if title_filter:
        df_filtered = df_filtered[
            df_filtered["title"].str.contains(title_filter, case=False)
        ]

    fig = px.bar(
        df_filtered, x="title", y="max_salary", title="Max Salary by Job Title"
    )
    fig.update_layout(xaxis={"categoryorder": "total descending"})
    fig.update_xaxes(tickangle=45)
    return fig
