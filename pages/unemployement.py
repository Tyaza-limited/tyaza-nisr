from data import (
    d_graph,
    line_graphs_for_trends_over_time,
    bar_charts_for_comparison,
    dates,
    year_2019,
    year_2020,
    year_2021,
    year_2022,
    year_2023,
    year_2024,
    stacked_area_chart,
    dd,
    heat_map_g,
    dual_axis_line_chart,
)
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
import dash

dash.register_page(__name__)

figures = d_graph()
default_value = next(iter(figures))

bar_charts = {
    "year_2019": bar_charts_for_comparison(dates[:4], year_2019),
    "year_2020": bar_charts_for_comparison(dates[4:][:4], year_2020),
    "year_2021": bar_charts_for_comparison(dates[8:][:4], year_2021),
    "year_2022": bar_charts_for_comparison(dates[12:][:4], year_2022),
    "year_2023": bar_charts_for_comparison(dates[16:][:4], year_2023),
    "year_2024": bar_charts_for_comparison(dates[20:][:4], year_2024),
}
tab1_content = html.Div(
    [
        dcc.Dropdown(
            id="figure-dropdown",
            options=[{"label": key, "value": key} for key in figures.keys()],
            value=default_value,
            clearable=False,
        ),
        dcc.Graph(id="selected-graph"),
    ],
    className="mt-4",
)

tab2_content = html.Div(
    [
        dcc.Dropdown(
            id="year-dropdown",
            options=[{"label": key, "value": key} for key in bar_charts.keys()],
            value=next(iter(bar_charts)),
            clearable=False,
        ),
        dcc.Graph(id="year-graph"),
    ],
    className="mt-4",
)
tab3_content = html.Div([dcc.Graph(figure=stacked_area_chart(dates, dd))])
fig1, fig2 = heat_map_g(dates, dd)
tab4_content = html.Div(
    [
        dcc.Graph(figure=fig1),
        html.Hr(),
        dcc.Graph(figure=fig2),
    ]
)
tab5_content = html.Div(
    [
        dcc.Graph(figure=dual_axis_line_chart(dates, dd)),
    ]
)


def layout(**kwargs):
    return html.Div(
        [
            dbc.Tabs(
                [
                    dbc.Tab(tab1_content, label="Increase over time"),
                    dbc.Tab(
                        tab2_content, label="Comparision of Labour force indicators"
                    ),
                    dbc.Tab(
                        tab3_content,
                        label="Combined Unemployment and Underemployment Rates",
                    ),
                    dbc.Tab(tab4_content, label="Unemployment Rate and NEET Over Time"),
                    dbc.Tab(
                        tab5_content,
                        label="Dual-Axis Line Chart of Labor Force Participation and Unemployment Rates",
                    ),
                ],
                className="mt-4",
            )
        ]
    )


@callback(
    Output("selected-graph", "figure"),
    Output("year-graph", "figure"),
    Input("figure-dropdown", "value"),
    Input("year-dropdown", "value"),
)
def update_graph(selected_figure, selected_year):
    figure = figures[selected_figure]
    year_figure = bar_charts[selected_year]
    return figure, year_figure
