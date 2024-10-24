from dash import Dash, dcc, callback, Output, Input, html
import lib.index

app = Dash()

app.layout = [
    html.H1(children='Employement over time in Rwanda', style={'textAlign':'center'}),
    dcc.Graph(figure=lib.index.summary())
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    print(12)

if __name__ == '__main__':
    app.run(debug=True)
