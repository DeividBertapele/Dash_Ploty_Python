from dash import Dash
from dash_html_components import Div, H1, P, H3
from dash_core_components import Graph
from random import randint

external_stylesheets = [
    'https://unpkg.com/terminal.css@0.7.2/dist/terminal.min.css',
]


app = Dash(__name__, external_stylesheets=external_stylesheets)

N = 20

database = {
    'index': list(range(N)),
    'maiores': [randint(1, 1000) for _ in range(N)]
}


app.layout = Div(
    children=[
        H1('Olá mundo'),
        P('Bem vindo ao Dash'),
        H3('Gráfico de Teste'),
        Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {
                        'y': database['maiores'],
                        'x': database['index'],
                        'name': 'Maiores'
                    },
                ],
                'layout': {
                    'title': 'Teste do Gráfico',
                    'paper_bgcolor': '#222225',
                    'titlefont':{
                        'size': 30,
                        'color': '#e8e9ed'
                    }
                },
            }
        )
    ]
)




if __name__ == '__main__':
    app.run_server(debug=True)
