from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


df = pd.read_csv('ecommerce_estatistica.csv')
lista_material = df['Material'].unique()
options = [{'label': material, 'value': material} for material in lista_material]

def criar_grafico(selecao_material):
    # Gráfico de Barras

    filtro_df = df[df['Material'].isin(selecao_material)]

    fig1 = px.bar(filtro_df, x='Gênero', y='Qtd_Vendidos_Cod', color='Temporada', barmode='group',
                  color_discrete_sequence=px.colors.qualitative.Bold, opacity=1)
    fig1.update_layout(
        title='Gênero por Quantidade Vendidos e Temporada',
        xaxis_title='Gênero',
        yaxis_title='Quantidade Vendidos',
        legend_title='Temporada',
        plot_bgcolor='rgba(222, 255, 253, 1)',  # Fundo interno
        paper_bgcolor='rgba(186, 245, 241, 1)'  # Fundo externo
    )

    fig2 = px.scatter_3d(filtro_df, x='Gênero', y='Qtd_Vendidos_Cod', z='Temporada', color='Temporada')
    fig2.update_layout(
        title='Gênero vs Quantidade Vendidos e Temporada',
        scene=dict(
            xaxis_title='Gênero',
            yaxis_title='Quantidade Vendidos',
            zaxis_title='Temporada'
        )
    )

    fig3 = px.line(filtro_df, x='Nota', y='Qtd_Vendidos_Cod', color='Gênero')
    fig3.update_layout(
        title='Quantidade Vendidos por Nota e Gênero',
        xaxis_title='Nota',
        yaxis_title='Quantidade Vendidos',
        legend_title='Gênero'

    )

    return fig1, fig2, fig3

def cria_app():
    # cria app
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1('Dashboard Interativo'),
        html.Div('''
        Interatividade entre os dados.
        '''),
        html.Br(),
        html.H2('Gráfico de Quantidade Vendidos por Temporada'),
        dcc.Checklist(
            id='id_selecao_material',
            options=options,
            value=[lista_material[0]],  # Definir valor padrão
        ),
        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_3d'),
        dcc.Graph(id='id_grafico_linha')
    ])
    return app

# Executa App
if __name__ == '__main__':
    app = cria_app()

    @app.callback(
        [
        Output('id_grafico_barra', 'figure'),
        Output('id_grafico_3d', 'figure'),
        Output('id_grafico_linha', 'figure')
        ],
        [Input('id_selecao_material', 'value')]
    )
    def atualiza_grafico(selecao_material):
        fig1, fig2, fig3 = criar_grafico(selecao_material)
        return [fig1, fig2, fig3]
    app.run_server(debug=True, port=8050)  # Default 8050
