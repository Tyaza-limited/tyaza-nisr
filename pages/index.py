import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from data import d_graph

dash.register_page(__name__, path="/")


figures = d_graph()

fig = figures["LU1-Unemployment rate (%)"]

layout = dbc.Container(
    children=[
        dbc.Row(
            dbc.Col(
                html.H1(
                    "Data Science for a Brighter Future: Tackling Youth Unemployment in Rwanda"
                ),
            ),
            className="mb-5",
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    "Youth unemployment is a pressing issue in Rwanda, leaving many young, talented individuals without opportunities to reach their full potential. This project aims to harness the power of data science to address this challenge head-on."
                ),
                width=12,
            ),
            className="mb-4",
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.H4("The Challenge: Youth Unemployment in Rwanda"),
                        html.P(
                            "Youth unemployment is a critical challenge in Rwanda, with many young people struggling to find jobs that match their skills and qualifications. Data science can play a pivotal role in analyzing job market trends, identifying skill gaps, and developing targeted strategies for employment."
                        ),
                    ]
                ),
                width=12,
            ),
            className="mb-4",
        ),
        dbc.Row(dbc.Col(dcc.Graph(figure=fig), width=12), className="mb-5"),
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.H4("Our Approach"),
                        html.P(
                            "Using advanced machine learning techniques and data analysis, our project aims to:"
                        ),
                        html.Ul(
                            [
                                html.Li(
                                    "Analyze job market trends and predict employment opportunities."
                                ),
                                html.Li(
                                    "Identify key skill gaps and offer targeted training programs."
                                ),
                            ]
                        ),
                    ]
                ),
                width=12,
            ),
            className="mb-4",
        ),
    ],
    fluid=True,
)
