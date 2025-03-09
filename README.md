# ProjetoEBAC - Dashboard-Interativo
### Projeto utilizando a biblioteca Plotly para criar gráficos interativos

Sejam bem-vindos ao ProjetoEBAC - Dashboard Interativo. Nesse projeto estarei apresentando a vocês três gráficos que foram criados utilizando a biblioteca Plotly e comandos em Python.

## Explicação do Dashboard
O código inicia com a criação de uma função onde são armazenadas as instruções de criação dos gráficos.

```
def criar_grafico(selecao_material):
```

Após as instruções para a criação dos gráficos criamos outra função que irá ser responsável pela criação do App.

```
def cria_app():
```

Por fim, escrevemos as instruções para inicializarmos o App

'''
if _name_ == '_main_':
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
'''
