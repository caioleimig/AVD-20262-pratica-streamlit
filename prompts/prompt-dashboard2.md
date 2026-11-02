
# Prompt de desenvolvimento: Dashboard 2 — KPIs (Aulas 22 e 23)

## Contexto

Dando continuidade ao projeto desenvolvido para a disciplina de Análise e Visualização de Dados, preciso implementar o segundo dashboard na mesma aplicação Streamlit, em uma nova aba (`st.tabs`).

A proposta deste dashboard é apresentar indicadores relevantes para a equipe de produto e marketing de um aplicativo de delivery, permitindo uma análise mais direta do comportamento e da satisfação dos clientes.

O planejamento visual e analítico já foi realizado por mim, com base na EDA desenvolvida na Aula 11. Preciso agora de apoio para transformar esse planejamento em componentes funcionais no Streamlit.

## Materiais e definições

- **Layout:** rascunho do Dashboard 2 elaborado por mim (`entregas/rascunho-dashboard2.png`).
- **Análise:** resultados da EDA disponíveis em `notebooks/eda-com-downloads.ipynb`, especialmente na seção 5.
- **Métricas:** quatro indicadores previamente selecionados e justificados por mim em `entregas/justificativa-metricas.md`:
  - Clientes no recorte;
  - Taxa de recompra;
  - Feedback positivo;
  - Idade média.
- **Filtros planejados:** gênero, ocupação, tipo de cliente e idade, posicionados na parte superior da aba.
- **Interação:** permitir que a seleção de uma ou mais faixas etárias no gráfico correspondente filtre os demais indicadores e visuais.

## Orientações para implementação

- Utilizar Streamlit e Altair em todos os gráficos, seguindo o guia `ALTAIR-CROSSFILTER.md` para implementar a seleção cruzada com `on_select="rerun"`.
- Apresentar as métricas com `st.metric`, incluindo deltas em relação aos valores da base completa.
- Manter entre 3 e 5 indicadores e apresentar pelo menos 3 gráficos complementares.
- Seguir a identidade visual definida em `.streamlit/config.toml`: laranja (`#D45F0A`) para respostas positivas e azul (`#3F6FB5`) para negativas.
- Considerar a legibilidade e a acessibilidade das cores.
- Tratar situações em que os filtros não retornem clientes: os KPIs devem apresentar "—", sem gerar erros na aplicação.

## Resultado esperado

Auxiliar na implementação do código da segunda aba no `app.py` e das funções necessárias em `src/graficos.py`, respeitando o layout e as definições já estabelecidas.

Também preparar testes de borda utilizando `st.testing.v1.AppTest`, especialmente para verificar o comportamento dos filtros e dos indicadores em situações sem resultados.