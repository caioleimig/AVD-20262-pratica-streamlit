
# Prompt de desenvolvimento: Dashboard 1 — Correlação e distribuição (Aula 21)

## Contexto

Sou aluno da disciplina de Análise e Visualização de Dados da CESAR School (2026.2) e estou desenvolvendo dois dashboards em Streamlit a partir da minha análise exploratória (EDA) da Aula 11.

O conjunto de dados utilizado foi o **Online Food Ordering Dataset**, disponível no Kaggle, com informações de 285 clientes de um aplicativo de delivery em Bangalore, após a remoção de duplicatas.

O primeiro dashboard tem como objetivo explorar a correlação e a distribuição das variáveis quantitativas e ordinais. Antes da implementação, elaborei um rascunho à mão com a organização dos elementos, os filtros e os gráficos que gostaria de apresentar.

A estrutura do projeto segue o modelo trabalhado na disciplina, com `app.py` na raiz, `src/data_loader.py` para leitura dos dados em `data/clean/dataset.csv` e diretórios separados para notebooks, entregas e prompts.

## Materiais e definições

- **Layout:** rascunho do Dashboard 1 elaborado por mim (`entregas/rascunho-dashboard1.png`).
- **Variáveis quantitativas e ordinais:** `idade`, `tamanho_familia`, `renda_nivel` (0–4), `escolaridade_nivel` (0–4), `latitude` e `longitude`.
- **Variável de classificação:** `pede_novamente` (Sim/Não).
- **Perguntas que orientam a análise:**
  - Quais variáveis apresentam relações entre si?
  - Como cada variável está distribuída?
  - As relações observadas mudam quando removemos valores extremos?
- **Organização visual planejada:** barra lateral com seletores de variáveis, método de correlação, filtro por classe e controles de intervalo. Na área principal, heatmap à esquerda e histogramas à direita.

## Orientações para implementação

- Utilizar Streamlit e Altair para a construção da aplicação e dos gráficos, sem utilizar Plotly.
- Restringir as alterações aos arquivos `app.py` e ao diretório `src/`.
- Carregar os dados por meio de `src/data_loader.py`, utilizando `@st.cache_data` e caminhos relativos.
- Implementar pelo menos um seletor de variáveis e um controle deslizante de intervalo.
- Garantir que a aplicação continue funcionando quando nenhuma, apenas uma ou duas ou mais variáveis forem selecionadas.
- Evitar o uso de `use_container_width`, por estar depreciado, e não utilizar CSS personalizado.

## Resultado esperado

Auxiliar na construção do código completo do `app.py`, seguindo a organização visual definida no meu rascunho. O código deve conter comentários curtos para separar as principais seções e uma explicação breve sobre a função de cada bloco, facilitando a compreensão e a manutenção da implementação.
