import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AdventureWorks Analytics", layout="wide")

st.title("📊 AdventureWorks - Data App (Item 9)")

# ======================================================
# Carregamento dos arquivos (fixos)
# ======================================================

FILES = {
    "fact_sales": "fact_sales.csv",
    "dim_product": "dim_product.csv",
    "dim_categories": "dim_categories.csv",
    "dim_calendar": "dim_calendar.csv"
}

dfs = {}

st.subheader("📁 Carregando arquivos")
for name, path in FILES.items():
    try:
        df = pd.read_csv(path)
        dfs[name] = df
        st.success(f"Carregado: {path} ({len(df)} linhas)")
    except Exception as e:
        st.error(f"Erro ao carregar {path}: {e}")

# ======================================================
# Mostrar estruturas
# ======================================================
st.subheader("🧱 Estrutura das tabelas")
for name, df in dfs.items():
    st.write(f"### {name}")
    st.write("Colunas:", list(df.columns))
    st.dataframe(df.head(), use_container_width=True)

# ======================================================
# Função auto-detectora de chaves
# ======================================================
def detect_key(df, keys):
    cols = df.columns.str.lower()
    for k in keys:
        if k in cols.values:
            return df.columns[list(cols).index(k)]
    return None

fact = dfs["fact_sales"]
dim_prod = dfs["dim_product"]
dim_cat = dfs["dim_categories"]
dim_cal = dfs["dim_calendar"]

# listas SEM quebra
product_keys = ["product", "product_id", "productkey", "product_key", "prod_id", "sku"]
category_keys = ["category", "category_id", "categorykey", "category_key", "cat_id"]
date_keys = ["date", "date_id", "datekey", "date_key", "time_id"]

product_key_fact = detect_key(fact, product_keys)
product_key_dim = detect_key(dim_prod, product_keys)

category_key_fact = detect_key(fact, category_keys)
category_key_dim = detect_key(dim_cat, category_keys)

date_key_fact = detect_key(fact, date_keys)
date_key_dim = detect_key(dim_cal, date_keys)
