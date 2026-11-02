
# Prompt de desenvolvimento: Dashboard 2 — KPIs (Aulas 22 e 23)

> **Resumo reconstruído, não transcrição literal.** Reescrevi este arquivo depois do uso, para resumir o que pedi à IA (Uso nº 5 da declaração assinada, [DECLARACAO_IA.pdf](DECLARACAO_IA.pdf)). Na prática, as quatro métricas foram escolhidas em colaboração com a IA, e a primeira versão da justificativa foi redigida por ela (Uso nº 3).

## Contexto

Dando continuidade ao projeto desenvolvido para a disciplina de Análise e Visualização de Dados, preciso implementar o segundo dashboard na mesma aplicação Streamlit, em uma nova aba (`st.tabs`).

A proposta deste dashboard é apresentar indicadores relevantes para a equipe de produto e marketing de um aplicativo de delivery, permitindo uma análise mais direta do comportamento e da satisfação dos clientes.

A organização geral do layout foi definida por mim, com base na EDA desenvolvida na Aula 11. Preciso agora de apoio para transformar esse planejamento em componentes funcionais no Streamlit.

## Materiais e definições

- **Layout:** wireframe do Dashboard 2 (`entregas/wireframe-dashboard2.png`). Defini a organização geral, e a IA desenhou a imagem (Uso nº 2).
- **Análise:** resultados da EDA disponíveis em `notebooks/eda-com-downloads.ipynb`, especialmente na seção 5.
- **Métricas:** quatro indicadores selecionados em discussão com a IA e justificados em `entregas/justificativa-metricas.md` (primeira versão redigida pela IA e revisada por mim):
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