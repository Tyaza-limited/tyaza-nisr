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
                    dbc.Row(
                        dbc.Col(
                            html.Div(
                                [
                                    html.P(
                                        "Reference: National Institute of Statistics of Rwanda (NISR), Labour Force Survey, Q2 2024."
                                    ),
                                    html.P(
                                        "Reference: https://www.kaggle.com/datasets/arshkon/linkedin-job-postings?resource=download"
                                    ),
                                    html.P(
                                        "© 2024 NISR hackerthon Data Science for Youth Unemployment Project. All Rights Reserved.",
                                        # className="text-muted",
                                    ),
                                    html.P(
                                        "This project is open-source and available under the MIT License.",
                                        # className="text-muted",
                                    ),
                                    html.P(
                                        [
                                            "View the source code on ",
                                            html.A(
                                                "GitHub",
                                                href="https://github.com/your-username/your-project-repo",
                                                target="_blank",
                                                className="text-light",
                                            ),
                                            ".",
                                        ],
                                    ),
                                    html.P(
                                        "Contributions and feedback are welcome! Please refer to the project's GitHub page for more information on how to contribute.",
                                        # className="text-muted",
                                    ),
                                    html.P(
                                        [
                                            "Contact us: ",
                                            html.A(
                                                "team@tyaza.org",
                                                href="mailto:team@tyaza.org",
                                                className="text-light",
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                            width=12,
                            className="text-center",
                        ),
                        className="mt-5",
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

if __name__ == "__main__":
    app.run(debug=True)
