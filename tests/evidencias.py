# [IA] Claude Code – evidências dos filtros do dashboard 2 (KPIs do app × cálculo direto no CSV)
"""Roda o app com várias combinações de filtros e compara os 4 KPIs exibidos com o
mesmo cálculo feito direto no CSV, sem passar pelo app.

Rode da raiz do projeto:  python tests/evidencias.py
"""
import sys
from pathlib import Path

import pandas as pd
from streamlit.testing.v1 import AppTest

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data/clean/dataset.csv")

GENEROS, OCUPACOES, TIPOS = ["Feminino", "Masculino"], ["Estudante", "Empregado(a)", "Autônomo(a)", "Do lar"], ["Novo", "Regular", "Frequente"]

CASOS = [
    ("Sem filtros (base completa)", {}),
    ("Só Feminino", {"genero": ["Feminino"]}),
    ("Só Masculino", {"genero": ["Masculino"]}),
    ("Só Estudante", {"ocupacao": ["Estudante"]}),
    ("Empregado(a) + Autônomo(a)", {"ocupacao": ["Empregado(a)", "Autônomo(a)"]}),
    ("Só Do lar (grupo pequeno)", {"ocupacao": ["Do lar"]}),
    ("Só tipo Novo (grupo pequeno)", {"tipo": ["Novo"]}),
    ("Idade 25 a 33", {"idade": (25, 33)}),
    ("Feminino + Estudante + Frequente + 18 a 24", {"genero": ["Feminino"], "ocupacao": ["Estudante"], "tipo": ["Frequente"], "idade": (18, 24)}),
    ("Idade 33 a 33 (extremo)", {"idade": (33, 33)}),
    ("Do lar + Masculino (sem clientes)", {"genero": ["Masculino"], "ocupacao": ["Do lar"]}),
    ("Nenhum gênero marcado (vazio)", {"genero": []}),
]


def esperado(f):
    d = df[df["genero"].isin(f.get("genero", GENEROS)) & df["ocupacao"].isin(f.get("ocupacao", OCUPACOES))
           & df["tipo_cliente"].isin(f.get("tipo", TIPOS)) & df["idade"].between(*f.get("idade", (18, 33)))]
    if d.empty:
        return ["—"] * 4
    return [str(len(d)), f"{(d['pede_novamente'] == 'Sim').mean() * 100:.1f}%".replace(".", ","),
            f"{(d['feedback'] == 'Positivo').mean() * 100:.1f}%".replace(".", ","), f"{d['idade'].mean():.1f} anos".replace(".", ",")]


def no_app(f):
    app = AppTest.from_file(str(RAIZ / "app.py"), default_timeout=60)
    app.run()
    if "genero" in f:
        app.pills(key="d2_genero").set_value(f["genero"])
    if "ocupacao" in f:
        app.multiselect(key="d2_ocupacao").set_value(f["ocupacao"])
    if "tipo" in f:
        app.pills(key="d2_tipo").set_value(f["tipo"])
    if "idade" in f:
        app.slider(key="d2_idade").set_value(f["idade"])
    app.run()
    assert not app.exception, app.exception
    return [str(m.value) for m in app.metric]


if __name__ == "__main__":
    print("| Combinação de filtros | Clientes | Recompra | Feedback positivo | Idade média | Confere com o CSV? |")
    print("|---|---|---|---|---|---|")
    falhas = 0
    for nome, filtros in CASOS:
        app_kpis, csv_kpis = no_app(filtros), esperado(filtros)
        ok = app_kpis == csv_kpis
        falhas += not ok
        print(f"| {nome} | {' | '.join(app_kpis)} | {'sim' if ok else f'NÃO (CSV: {csv_kpis})'} |")
    sys.exit(1 if falhas else 0)
