
# Declaração de Uso de IA (resumo)

**Nome:** Caio Leimig Rodrigues da Silva  
**Data:** 02/11/2026 (Aulas 21, 22 e 23: dashboards em Streamlit)

> A declaração oficial, preenchida e assinada (gov.br), é [`DECLARACAO_IA.pdf`](DECLARACAO_IA.pdf). Este arquivo é só um resumo dela. Se houver qualquer diferença, vale o PDF.

## Ferramentas utilizadas

- **Claude Code** (extensão do VS Code, modelo Claude Opus 5.5): notebook de pipeline, esqueleto do `app.py`, Dashboards 1 e 2, wireframes, testes, README, otimização do código e revisões (Usos nº 1 a 5).
- **Skill oficial do Streamlit** (`streamlit skills --yes`): usada pelo Claude Code para escrever o código do app no padrão atual da biblioteca.
- **Claude (chat, claude.ai)**, modelo Claude Opus 5.5: EDA da Aula 11 (`notebooks/eda.ipynb`) e, em 01–02/11, revisão das regras do projeto e ajustes de texto em `entregas/` (Usos nº 5 e 6).

## Resumo dos usos

| Nº | Data | Parte | O que a IA fez |
|---|---|---|---|
| 1 | 29–30/10 | Estrutura do repositório, pipeline, `app.py` (esqueleto e Dashboard 1), `src/`, `.streamlit/config.toml` | Pedi apoio em boa parte da atividade ("me ajude com esqueletos .py, gráficos, design e apoio com pandas"). Aproveitei a estrutura, o pipeline, o cache, a sidebar, o heatmap e os histogramas. Pedi Spearman para as variáveis ordinais, troquei a paleta para laranja e azul e rejeitei o mapa com a localização dos clientes. |
| 2 | 31/10 | `entregas/wireframe-dashboard1.png` e `wireframe-dashboard2.png` | **Fora do previsto:** os dois rascunhos entregues foram desenhados pela IA. Defini a organização geral (separação das telas, posição dos filtros, disposição dos indicadores), e a IA fez a elaboração visual. |
| 3 | 31/10 | Dashboard 2 (`app.py`, `src/graficos.py`) e `entregas/justificativa-metricas.md` | **Fora do permitido:** as quatro métricas (clientes no recorte, taxa de recompra, feedback positivo e idade média) foram escolhidas em colaboração com a IA, e a primeira versão da justificativa foi redigida por ela. Depois revisei e reescrevi o texto com minhas palavras. A IA implementou os KPIs, os gráficos, os filtros e a seleção cruzada. Defini que o delta da idade média aparece em cinza. |
| 4 | 30/10 | Dado tratado, pipeline, `src/`, `app.py`, testes, `requirements*.txt`, READMEs, marcações `# [IA]` | Otimização do código, depuração e revisão de textos: remoção de latitude, longitude e Pin code, separação das dependências, simplificação do código e marcações `# [IA]`. |
| 5 | 01–02/11 | Arquivos de `prompts/`, nota de autoria da justificativa, `entregas/README.md`, declaração | Revisão de textos e conferência das regras. Os arquivos `prompt-esqueleto-dashboard1.md` e `prompt-dashboard2.md` são **resumos reconstruídos** depois do uso, não transcrições literais dos prompts. |
| 6 | 01/11 | `notebooks/eda.ipynb` (EDA da Aula 11) | Estrutura do notebook e código de cada etapa (descritiva, Shapiro-Wilk, IQR, testes de grupos, Qui-quadrado, fairness, correlograma). As decisões de interpretação e as respostas às perguntas de discussão são minhas. |

## Validação

- Conferi os valores com a minha EDA: 285 linhas no dado tratado, Spearman idade × renda ≈ 0,57, recompra de 76,1%, feedback positivo de 81,1% e idade média de 24,7 anos.
- Testei a seleção cruzada clicando nas faixas etárias e rodei os testes de borda com `python tests/test_app.py`.
- Comparei o app final com os wireframes.
