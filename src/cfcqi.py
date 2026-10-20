"""Shared helpers for the CFCQI project."""
from __future__ import annotations
import numpy as np
import pandas as pd

ITEMS = [f"item{i}" for i in range(1, 13)]

ITEM_LABELS = {
    "item1": "Current financial performance",
    "item2": "Current financial position",
    "item3": "Current cash flows",
    "item4": "Anticipated future financial performance",
    "item5": "Anticipated future financial position",
    "item6": "Anticipated future cash flows",
    "item7": "Capital expenditure / allocation",
    "item8": "Asset valuations & impairment",
    "item9": "Provisions, contingencies & commitments",
    "item10": "Carbon pricing / ETS / regulatory costs",
    "item11": "Financial planning integration",
    "item12": "Quantified scenario analysis",
}

def validate_coding(df):
    errors = []
    for col in ITEMS:
        if col not in df.columns:
            errors.append(f"missing column {col}")
            continue
        bad = df[~df[col].isin([0, 1, 2])]
        if len(bad):
            errors.append(f"{col}: {len(bad)} values outside {{0,1,2}}")
    if "firm_id" in df.columns and df["firm_id"].isna().any():
        errors.append("firm_id has missing values")
    return errors

def compute_cfcqi(df):
    df = df.copy()
    df["raw_score"] = df[ITEMS].sum(axis=1)
    df["cfcqi"] = (df["raw_score"] / 24 * 100).round(1)
    return df

def percent_agreement(a, b):
    a = np.asarray(a); b = np.asarray(b)
    return float((a == b).mean())

def weighted_kappa(a, b):
    """Quadratic-weighted Cohen's kappa. Uses sklearn when available,
    otherwise a pure-numpy implementation (identical formula)."""
    try:
        from sklearn.metrics import cohen_kappa_score
        return float(cohen_kappa_score(a, b, weights="quadratic"))
    except ImportError:
        pass
    a = np.asarray(a, dtype=int)
    b = np.asarray(b, dtype=int)
    cats = np.unique(np.concatenate([a, b]))
    k = len(cats)
    idx = {c: i for i, c in enumerate(cats)}
    O = np.zeros((k, k))
    for x, y in zip(a, b):
        O[idx[x], idx[y]] += 1
    O = O / O.sum()
    E = np.outer(O.sum(axis=1), O.sum(axis=0))
    w = np.fromfunction(lambda i, j: (i - j) ** 2 / (k - 1) ** 2, (k, k))
    return float(1.0 - (w * O).sum() / (w * E).sum())
