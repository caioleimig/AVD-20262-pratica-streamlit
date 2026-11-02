# Justificativa das métricas — Dashboard 2

> **Autoria e uso de IA:** As quatro métricas deste dashboard (clientes no recorte, taxa de recompra, feedback positivo e idade média) foram escolhidas **em colaboração com a IA** (Claude Code): discuti com ela quais indicadores poderiam responder à pergunta do Dashboard 2 e ajustamos juntos a seleção final. A **primeira versão desta justificativa também foi redigida pela IA**. Depois, revisei e reescrevi o texto com minhas palavras, com base na minha EDA e nos objetivos do projeto, e conferi os valores citados com os dados tratados. Esse uso está registrado como fora do permitido no **Uso nº 3** da declaração assinada ([`prompts/DECLARACAO_IA.pdf`](../prompts/DECLARACAO_IA.pdf)).

**Dataset:** Online Food Ordering Dataset (Kaggle), com 285 clientes após a remoção de duplicatas (ver `notebooks/eda.ipynb` e `notebooks/eda-com-downloads.ipynb`).

**Público-alvo do dashboard:** equipe de produto, marketing e CRM do aplicativo de delivery. São profissionais responsáveis por decisões relacionadas a campanhas, segmentação de clientes e melhorias no serviço, que precisam de indicadores objetivos e de fácil interpretação, sem necessariamente precisar consultar histogramas ou testes estatísticos.

**Pergunta que o dashboard responde:** *Quem são os clientes que pediriam novamente e quem está insatisfeito?*

**Definição dos widgets:** Os filtros e mecanismos de interação foram planejados por mim antes da elaboração do rascunho `wireframe-dashboard2.png`. A proposta foi permitir que o usuário explore diferentes segmentos e observe como as métricas se comportam em cada recorte.

- Barra de filtros no topo: gênero (`st.pills`), ocupação (`st.multiselect`), tipo de cliente (`st.pills`) e idade (`st.slider`).
- Clique no gráfico de faixa etária (seleção Altair com `on_select="rerun"`): permite selecionar uma ou mais faixas etárias e aplicar esse recorte aos KPIs e aos outros três gráficos.

> **Observação sobre `Output`:** O dataset não documenta formalmente essa coluna. A interpretação adotada na minha análise foi a de que `Output = Yes` indica que o cliente pediria novamente pelo aplicativo. Essa ressalva também está apresentada no próprio dashboard, na seção "Como ler este dashboard".

---

## Métrica 1: Clientes no recorte

- **Variável:** contagem de linhas após a aplicação dos filtros, considerando como base os 285 clientes.
- **Tipo:** contagem.
- **O que mede:** quantidade de clientes que atendem aos filtros e à faixa etária selecionada, acompanhada do percentual que representam em relação à base completa.
- **Por que foi escolhida:** defini essa métrica para contextualizar todas as demais. Uma taxa de 90% calculada sobre 9 pessoas não possui o mesmo peso de uma taxa calculada sobre 140. Durante minha EDA, identifiquei grupos com quantidades bastante reduzidas, como os 9 clientes classificados como "Do lar" e os 18 classificados como "Novo". Por isso, considerei importante apresentar o tamanho de cada segmento antes da interpretação dos indicadores.
- **Público-alvo:** todos os usuários do dashboard.
- **Qual decisão pode ser apoiada por essa métrica?** Avaliar se determinado segmento possui tamanho suficiente para justificar uma campanha ou ação específica, além de identificar resultados baseados em grupos muito pequenos.
- **O que comunica ao público-alvo:** "Estamos analisando N pessoas, correspondentes a X% dos clientes". Dessa forma, o usuário conhece o tamanho do segmento antes de interpretar suas taxas.

## Métrica 2: Taxa de recompra

- **Variável:** `pede_novamente` (variável original `Output`, com valores Sim/Não).
- **Tipo:** proporção (% de respostas "Sim"), acompanhada do delta em pontos percentuais em relação à base completa (76,1%).
- **O que mede:** proporção de clientes do segmento que indicaram que pediriam novamente pelo aplicativo.
- **Por que foi escolhida:** selecionei essa variável por ser o principal resultado investigado na minha EDA e o indicador mais próximo de retenção dentro do contexto de negócio de um aplicativo de delivery. Na análise exploratória, identifiquei diferenças relevantes na recompra entre as faixas etárias (Qui-quadrado, p≈0,0001): aproximadamente 80–88% até 24 anos, contra 62–65% a partir dos 25 anos. Esse resultado motivou sua utilização como principal indicador de desempenho do Dashboard 2.
- **Público-alvo:** equipe de marketing/CRM e liderança de produto.
- **Qual decisão pode ser apoiada por essa métrica?** Identificar segmentos que apresentam recompra abaixo da média e que poderiam receber ações de retenção, como cupons, programas de fidelidade ou comunicações direcionadas.
- **O que comunica ao público-alvo:** "De cada 100 clientes deste grupo, X indicaram que pediriam novamente", permitindo comparar o resultado com a média geral da base.

## Métrica 3: Feedback positivo

- **Variável:** `feedback` (Positivo/Negativo).
- **Tipo:** proporção (% de respostas "Positivo"), acompanhada do delta em pontos percentuais em relação à base completa (81,1%).
- **O que mede:** proporção de clientes do segmento que avaliaram positivamente o serviço.
- **Por que foi escolhida:** considerei importante analisar satisfação e recompra separadamente, pois representam dimensões diferentes da experiência do cliente. Um cliente pode avaliar positivamente o serviço sem necessariamente voltar a comprar, assim como a recompra não significa, por si só, satisfação. Na minha EDA, identifiquei associação entre feedback e ocupação (Qui-quadrado, p≈0,011), o que justificou a inclusão de uma análise segmentada por esse atributo. Também observei que o tipo de cliente não apresentou associação significativa com a recompra (p≈0,864).
- **Público-alvo:** equipe de produto e operações, especialmente profissionais envolvidos com qualidade da entrega e atendimento.
- **Qual decisão pode ser apoiada por essa métrica?** Identificar segmentos com maior proporção de avaliações negativas e priorizar melhorias no serviço ou pesquisas qualitativas para compreender os motivos da insatisfação, como nos grupos de empregados e autônomos.
- **O que comunica ao público-alvo:** "X% dos clientes deste grupo avaliaram o serviço positivamente", permitindo observar a satisfação independentemente da intenção de recompra.

## Métrica 4: Idade média

- **Variável:** `idade` (anos).
- **Tipo:** média, acompanhada do delta em anos em relação à média da base completa (24,7 anos).
- **O que mede:** perfil etário dos clientes pertencentes ao segmento selecionado.
- **Por que foi escolhida:** a idade foi uma das variáveis que mais diferenciou os clientes que indicaram que pediriam novamente daqueles que não indicaram essa intenção (24,3 contra 25,9 anos; Mann-Whitney, p<0,001). Por esse motivo, decidi apresentar a idade média junto à taxa de recompra, permitindo observar o perfil etário de cada recorte e explorar a relação identificada durante a EDA. O delta é apresentado em cinza propositalmente, pois uma idade maior ou menor não representa, isoladamente, um resultado positivo ou negativo.
- **Público-alvo:** equipe de marketing, principalmente para segmentação e adequação da linguagem das campanhas.
- **Qual decisão pode ser apoiada por essa métrica?** Compreender o perfil etário dos segmentos e avaliar possíveis adaptações no público e na comunicação das campanhas, considerando o comportamento de recompra observado na análise.
- **O que comunica ao público-alvo:** "O cliente médio deste grupo tem X anos", indicando se o segmento é mais jovem ou mais velho em relação à média geral.

---

## Visuais complementares às métricas

| Visual | Variável agrupada | Justificativa |
|---|---|---|
| Taxa de recompra por faixa etária (clicável) | `faixa_etaria` (mesmas faixas utilizadas na EDA) | Apresenta o principal achado da análise exploratória: a redução da recompra a partir dos 25 anos. Também funciona como filtro cruzado para os KPIs e os demais gráficos. |
| Feedback por ocupação (100% empilhado) | `ocupacao` × `feedback` | Permite observar a distribuição de avaliações positivas e negativas entre ocupações, explorando a associação identificada na EDA. |
| Taxa de recompra por renda mensal | `renda_mensal` | Permite investigar o comportamento de recompra entre diferentes faixas de renda. A inclusão foi motivada também pela correlação observada entre renda e idade (Spearman ≈ 0,57), possibilitando explorar essas características em conjunto. |
| Recompra por tipo de cliente (contagem) | `tipo_cliente` × `pede_novamente` | Permite comparar a quantidade de clientes que indicaram intenção de recompra em cada tipo de cliente, contextualizando os grupos e explorando o resultado da EDA de que a frequência de uso, isoladamente, não apresentou associação significativa com a recompra. |

---

## Considerações sobre a elaboração

A seleção das quatro métricas foi feita em colaboração com a IA, e a primeira versão desta justificativa foi redigida por ela, como descrito na nota de autoria no início do documento. Depois, revisei o texto com base na minha análise exploratória e conferi os números citados (76,1% de recompra, 81,1% de feedback positivo e 24,7 anos de idade média na base completa) com os dados tratados. A IA também implementou os KPIs, os gráficos, os filtros e a seleção cruzada no Streamlit. Defini que o delta da idade média aparece em cinza. O registro completo está nos Usos nº 2 e 3 da declaração assinada ([`prompts/DECLARACAO_IA.pdf`](../prompts/DECLARACAO_IA.pdf)).