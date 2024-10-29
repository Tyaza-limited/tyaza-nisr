from dash import Dash, html, dcc, Output, Input
from data import d_graph, line_graphs_for_trends_over_time, bar_charts_for_comparison, dates, year_2019, year_2020, year_2021, year_2022, year_2023, year_2024
app = Dash(__name__)

figures = d_graph()


# Get the first key dynamically for the default value
default_value = next(iter(figures))

bar_charts = dict()
bar_charts['year_2019'] = bar_charts_for_comparison(dates[:4], year_2019)
bar_charts['year_2020'] = bar_charts_for_comparison(dates[4:][:4], year_2020)
bar_charts['year_2021'] = bar_charts_for_comparison(dates[8:][:4], year_2021)
bar_charts['year_2022'] = bar_charts_for_comparison(dates[12:][:4], year_2022)
bar_charts['year_2023'] = bar_charts_for_comparison(dates[16:][:4], year_2023)
bar_charts['year_2024'] = bar_charts_for_comparison(dates[20:][:4], year_2024)

# Define the layout of the app
app.layout = html.Div([
    dcc.Dropdown(
        id='figure-dropdown',
        options=[{'label': key, 'value': key} for key in figures.keys()],
        value=default_value,  # Use the first key as the default value
        clearable=False
    ),
    dcc.Graph(id='selected-graph'),
    dcc.Graph(
        id="line_graphs_for_trends_over_time",
        figure=line_graphs_for_trends_over_time()
    ),
#  dcc.Dropdown(
#         id='year-dropdown',
#         options=[{'label': year, 'value': year} for year in data.keys()],
#         value='2024',  # Default value set to 2024
#         clearable=False
#     ),
#     dcc.Graph(id='year-graph')
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': key, 'value': key} for key in bar_charts.keys()],
        value=next(iter(bar_charts)),  # Use the first key as the default value
        clearable=False
    ),
    dcc.Graph(id='selected-graph'),

])

# @app.callback(
#     Output('selected-graph', 'figure'),
#     Output('selected-graph', 'figure'),
#     Input('figure-dropdown', 'value'),
#     Input('year-dropdown', 'value'),
# )

# def update_graph(selected_figure):
#     return figures[selected_figure]

if __name__ == '__main__':
    app.run(debug=True)
