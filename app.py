import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.LUX], use_pages=True)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Youth", href="/youth")),
        dbc.NavItem(dbc.NavLink("Unemployement", href="/unemployement")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("About project", href="/about"),
                dbc.DropdownMenuItem("About Team", href="/team"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="TYaza team",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = html.Div(
    [
        navbar,
        html.Div(
            [
                dbc.Container(
                    [
                        dash.page_container,
                    ]
                ),
                html.Footer(
                    dbc.Container(
                        "Reference: National Institute of Statistics of Rwanda (NISR), Labour Force Survey, Q2 2024."
                    ),
                    className="mt-4 py-4 bg-dark text-light",
                ),
            ],
            style={"min-height": "calc(100vh - 7rem)"},
            className="d-flex flex-column justify-content-between",
        ),
    ],
    className="d-grid gap-4",
)

server = app.server

# if __name__ == "__main__":
#     app.run(debug=True)
