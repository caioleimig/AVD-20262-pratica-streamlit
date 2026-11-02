
# Declaração de Uso de IA

**Nome:** Caio Leimig Rodrigues da Silva  
**Data:** 29/10/2026 (Aulas 21, 22 e 23: dashboards em Streamlit)

## Ferramentas utilizadas

- **Claude Code:** utilizado no VS Code, com o modelo Claude Opus 5.5 e as skills do Streamlit (`streamlit skills`), como apoio ao desenvolvimento técnico da aplicação.
- **Claude (chat):** utilizado durante a EDA da Aula 11, conforme declarado no notebook correspondente.

## Prompt inicial utilizado

O pedido inicial foi realizado com os slides das três aulas sobre Streamlit (partes 1, 2 e 3) anexados:

> "Com base nesses 3 PDFs, me ajude a fazer essa atividade montando a estrutura de repositório necessária."

Posteriormente, enviei minha EDA da Aula 11 (Online Food Delivery) como referência para o desenvolvimento dos dashboards.

Os prompts estruturados, contendo contexto, entradas, restrições e formato esperado para cada etapa, estão disponíveis nos seguintes arquivos:

- [`prompt-esqueleto-dashboard1.md`](prompt-esqueleto-dashboard1.md)
- [`prompt-dashboard2.md`](prompt-dashboard2.md)

## Para que a IA foi utilizada

- Auxílio na estruturação do pipeline de dados (`notebooks/eda-com-downloads.ipynb`), do arquivo `app.py`, dos módulos em `src/` e dos testes.
- Implementação técnica dos componentes e das métricas do Dashboard 2 no Streamlit. **A escolha das quatro métricas, os critérios de seleção, as justificativas e a interpretação dos resultados da EDA foram realizados por mim**, com base na minha própria análise do conjunto de dados.
- Revisão de ortografia e clareza textual do arquivo `entregas/justificativa-metricas.md`, cujo conteúdo e decisões analíticas foram elaborados por mim. A IA não escolheu, propôs ou justificou as métricas.
- Digitalização dos layouts em wireframes (`entregas/wireframe-dashboard*.png`). Os rascunhos originais à mão (`entregas/rascunho-dashboard*`) foram elaborados por mim, sem utilização de IA.
- Apoio na organização do README e na estruturação do repositório.

## O que foi aceito, modificado ou rejeitado

- **Aceito:** código responsável por transformar meus rascunhos em interfaces funcionais, incluindo as duas abas, os filtros na barra lateral do Dashboard 1, os filtros no topo do Dashboard 2 e a implementação das quatro métricas previamente definidas por mim. Também foram aproveitados o uso de cache e os caminhos relativos.
- **Modificado:** solicitei a inclusão de renda e escolaridade como variáveis ordinais, utilizando a correlação de Spearman; substituí a paleta de cores por laranja e azul, buscando melhorar a legibilidade para pessoas com daltonismo; e solicitei correções na formatação dos deltas dos KPIs.
- **Rejeitado:** a implementação de um mapa com a localização dos clientes, pois latitude, longitude e `Pin code` foram removidos do conjunto de dados tratado por precaução. Também rejeitei a reprodução do modelo de Dashboard 1 presente no repositório de referência, optando pelo layout que havia planejado nos meus próprios rascunhos.

## Validação realizada

Conferi os resultados apresentados pela aplicação com os dados e resultados da minha EDA, verificando, entre outros valores, a existência de 285 linhas no conjunto de dados tratado e a proporção de 81,1% de feedback positivo.

Também executei os testes de borda por meio do comando:

```bash
python tests/test_app.py
```

A validação teve como objetivo verificar a consistência dos resultados apresentados e o funcionamento dos componentes implementados.

## Delimitação da autoria das decisões analíticas

As decisões relacionadas à análise dos dados foram realizadas por mim. Isso inclui a definição do público-alvo do Dashboard 2, a pergunta de negócio que orienta sua construção, a seleção das quatro métricas, a escolha dos gráficos complementares, os critérios de segmentação e as justificativas apresentadas em `entregas/justificativa-metricas.md`.

A IA foi utilizada como ferramenta de apoio técnico para implementar essas decisões no Streamlit, além de auxiliar na organização e revisão de partes do projeto. **Não utilizei IA para escolher as métricas, interpretar os resultados da EDA ou elaborar as justificativas analíticas do Dashboard 2.**