# Evidências de testes e validação

Registro do que foi testado nos dois dashboards e dos resultados obtidos (02/11/2026, Streamlit 1.66.1).

> Os scripts de teste e esta página foram escritos com apoio do Claude Code (Usos nº 4 e 5 da [declaração assinada](../prompts/DECLARACAO_IA.pdf)). Os valores abaixo foram gerados rodando os scripts, não digitados à mão.

## 1. Testes automáticos de borda (`tests/test_app.py`)

Rode da raiz do projeto: `python tests/test_app.py`. Ele usa `st.testing.v1.AppTest`, que executa o app sem abrir o navegador.

| Caso | O que é testado | Resultado esperado | Resultado |
|---|---|---|---|
| Padrão | App abre com os filtros iniciais | 2 abas, 4 KPIs, frase "Par mais forte" no heatmap, sem erro | Passou |
| 0 variáveis | Dashboard 1 sem nenhuma variável selecionada | Avisos "pelo menos 2 variáveis" (correlação) e "pelo menos 1 variável" (distribuição) | Passou |
| 1 variável | Só `idade` selecionada | Aviso na correlação, histograma continua aparecendo | Passou |
| 4 variáveis × 3 métodos | Spearman, Pearson e Kendall + "separar por recompra" + "remover outliers (IQR)" | Nenhuma exceção em nenhuma combinação | Passou |
| Intervalo estreito | Idade 33–33 (1 cliente) e tamanho da família 1–1 (variável constante) | Avisos "Poucos clientes" e "Sem variação" no lugar de erro | Passou |
| Dashboard 2 vazio | Ocupação "Do lar" + nenhum gênero marcado | Os 4 KPIs mostram "—" e aparece o aviso "Nenhum cliente atende" | Passou |

## 2. KPIs do Dashboard 2 com filtros (`tests/evidencias.py`)

Rode com `python tests/evidencias.py`. Para cada combinação, o script aplica os filtros no app e lê os 4 KPIs exibidos. Depois, calcula os mesmos valores direto no `data/clean/dataset.csv` com pandas, sem passar pelo app, e compara os dois.

| Combinação de filtros | Clientes | Recompra | Feedback positivo | Idade média | Confere com o CSV? |
|---|---|---|---|---|---|
| Sem filtros (base completa) | 285 | 76,1% | 81,1% | 24,7 anos | sim |
| Só Feminino | 121 | 74,4% | 83,5% | 24,7 anos | sim |
| Só Masculino | 164 | 77,4% | 79,3% | 24,6 anos | sim |
| Só Estudante | 144 | 87,5% | 88,2% | 22,8 anos | sim |
| Empregado(a) + Autônomo(a) | 132 | 63,6% | 72,7% | 26,3 anos | sim |
| Só Do lar (grupo pequeno) | 9 | 77,8% | 88,9% | 30,3 anos | sim |
| Só tipo Novo (grupo pequeno) | 18 | 72,2% | 77,8% | 25,1 anos | sim |
| Idade 25 a 33 | 131 | 64,1% | 74,8% | 27,3 anos | sim |
| Feminino + Estudante + Frequente + 18 a 24 | 18 | 94,4% | 94,4% | 22,6 anos | sim |
| Idade 33 a 33 (extremo) | 1 | 0,0% | 0,0% | 33,0 anos | sim |
| Do lar + Masculino (sem clientes) | — | — | — | — | sim |
| Nenhum gênero marcado (vazio) | — | — | — | — | sim |

Observações:

- **"Idade 33 a 33"** mostra 0% de recompra calculado sobre **1 cliente**. É por isso que o KPI "Clientes no recorte" fica ao lado das taxas: ele mostra quantas pessoas existem por trás de cada percentual.
- **"Do lar + Masculino"** fica vazio porque não há nenhum cliente do sexo masculino com ocupação "Do lar" no dataset. O app mostra "—" sem gerar erro.

## 3. Seleção cruzada (clique no gráfico de faixa etária)

O `AppTest` não consegue simular cliques em gráficos Altair, por isso este teste é manual. A tabela traz o valor esperado de cada seleção, calculado direto no CSV com todos os filtros do topo abertos.

| Faixa(s) clicada(s) | Clientes (% da base) | Recompra | Feedback positivo | Idade média |
|---|---|---|---|---|
| 18-21 | 30 (10,5%) | 80,0% | 80,0% | 20,4 anos |
| 22-24 | 124 (43,5%) | 87,9% | 87,9% | 23,0 anos |
| 25-27 | 84 (29,5%) | 65,5% | 79,8% | 25,7 anos |
| 28+ | 47 (16,5%) | 61,7% | 66,0% | 30,1 anos |
| 25-27 + 28+ (shift + clique) | 131 (46,0%) | 64,1% | 74,8% | 27,3 anos |

A captura [`docs/img/dashboard2.png`](img/dashboard2.png), com a faixa 25-27 selecionada, mostra exatamente os valores da linha 25-27: 84 clientes, 29,5% da base, 65,5%, 79,8% e 25,7 anos.

Roteiro para conferir no app (`streamlit run app.py`, aba Dashboard 2):

- [ ] Clicar em cada barra e conferir os 4 KPIs com a tabela acima.
- [ ] Shift + clique em 25-27 e 28+ e conferir a última linha.
- [ ] Os gráficos "Feedback por ocupação", "Recompra por renda" e "Recompra por tipo de cliente" mudam junto com os KPIs.
- [ ] O gráfico de faixa etária continua mostrando todas as barras, com a selecionada destacada.
- [ ] Clicar numa área vazia do gráfico limpa a seleção e os KPIs voltam aos valores sem recorte.
- [ ] Com uma faixa selecionada, aplicar um filtro do topo que zere o recorte: os KPIs mostram "—" e os gráficos mostram "Sem clientes no recorte selecionado".

## 4. Conferência dos números citados nos textos

Valores recalculados a partir de `data/clean/dataset.csv` e comparados com o README, a justificativa das métricas e a EDA.

| Afirmação | Valor citado | Valor recalculado | Confere? |
|---|---|---|---|
| Clientes após remover duplicatas | 285 | 285 | sim |
| Taxa de recompra da base | 76,1% | 76,1% | sim |
| Feedback positivo da base | 81,1% | 81,1% | sim |
| Idade média da base | 24,7 anos | 24,7 anos | sim |
| Recompra até 24 anos / a partir de 25 | 80–88% / 62–65% | 80,0% e 87,9% / 65,5% e 61,7% | sim |
| Qui-quadrado faixa etária × recompra | p ≈ 0,0001 | p = 0,0001 | sim |
| Qui-quadrado ocupação × feedback | p ≈ 0,011 | p = 0,0107 | sim |
| Qui-quadrado tipo de cliente × recompra | p ≈ 0,864 | p = 0,864 | sim |
| Idade média: pediria novamente × não pediria | 24,3 × 25,9 anos, Mann-Whitney p < 0,001 | 24,3 × 25,9 anos, p ≈ 0,00001 | sim |
| Spearman idade × renda | ≈ 0,57 | 0,572 (p ≈ 3e-26) | sim |
| Empregados e autônomos com mais feedback negativo | — | 26,6% e 28,9%, contra ~11–12% nos demais grupos | sim |
| Grupos pequenos "Do lar" e "Novo" | 9 e 18 | 9 e 18 | sim |
| Todos os clientes "Novo" têm família de 1 pessoa | — | sim (único valor: 1) | sim |

Correções feitas nesta revisão:

- O README dizia que "a base é majoritariamente composta por estudantes sem renda". Estudantes sem renda são 122 de 285 (43%), não a maioria. O texto agora diz que cerca de metade da base é de estudantes (144) e que 122 deles não têm renda.
- O Dashboard 1 classificava r = 0,57 como correlação "forte". A escala foi alinhada à do notebook de referência da disciplina (|r| < 0,3 fraca, 0,3–0,7 moderada, > 0,7 forte), e agora o par idade × renda aparece como "moderada".
- O README ganhou uma ressalva de que os resultados mostram associações, não causa e efeito.

## 5. Deploy

- App publicado: <https://avd-delivery-caioleimig.streamlit.app/>
- `requirements.txt` exige `streamlit>=1.66`, porque o app usa parâmetros que não existem em versões anteriores (`required` no `segmented_control`, `alt` nos gráficos e tabelas).
- [ ] Abrir o link numa janela anônima e confirmar que o app carrega sem pedir login (acesso público).
