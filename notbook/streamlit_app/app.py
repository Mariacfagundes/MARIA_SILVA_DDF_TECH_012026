# ============================================================
# ITEM 9 – DATA APP (Exploração com Streamlit)
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import re
from collections import Counter

# ------------------------------------------------------------
# Funções auxiliares para similaridade de texto (usando apenas NumPy)
# ------------------------------------------------------------
def text_to_vector(text):
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

def cosine_sim(text1, text2):
    vec1 = text_to_vector(text1)
    vec2 = text_to_vector(text2)
    all_words = set(vec1.keys()).union(set(vec2.keys()))
    v1 = np.array([vec1.get(word, 0) for word in all_words])
    v2 = np.array([vec2.get(word, 0) for word in all_words])
    dot = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot / (norm_v1 * norm_v2) if norm_v1 and norm_v2 else 0.0

# ------------------------------------------------------------
# Carregar dados (arquivos estão na mesma pasta do app.py)
# ------------------------------------------------------------
products = pd.read_csv("dim_product.csv")
categories = pd.read_csv("dim_categories.csv")
sales = pd.read_csv("fact_sales.csv")
calendar = pd.read_csv("dim_calendar.csv")

# ------------------------------------------------------------
# Interface Streamlit
# ------------------------------------------------------------
st.title("Exploração de Dados - AdventureWorks")

# Mostrar tabela de produtos
st.subheader("Produtos disponíveis")
st.dataframe(products.head())

# Preço médio por categoria
st.subheader("Preço médio por categoria")

# Ajuste de chaves: verifique os nomes reais das colunas nos CSVs
df_cat = products.merge(
    categories,
    left_on="ProductCategoryKey",   # ajuste conforme o nome real da coluna
    right_on="CategoryKey",         # ajuste conforme o nome real da coluna
    how="left"
)

df_price_cat = df_cat.groupby("CategoryName")["ProductPrice"].mean().reset_index()
st.bar_chart(df_price_cat.set_index("CategoryName"))

# ------------------------------------------------------------
# Similaridade entre produtos (usando descrição, sem scikit-learn nem SciPy)
# ------------------------------------------------------------
st.subheader("Similaridade entre produtos (descrição)")

# Se não houver coluna "ProductDescription", ajuste para a coluna correta
descriptions = products["ProductDescription"].fillna("").tolist()

similarities = []
for i in range(1, len(descriptions)):
    sim = cosine_sim(descriptions[0], descriptions[i])
    similarities.append((i, sim))

# Ordenar pelos mais similares
similarities_sorted = sorted(similarities, key=lambda x: x[1], reverse=True)[:5]
similar_products = products.iloc[[i for i, _ in similarities_sorted]][["ProductName", "ProductDescription"]]

st.write("Produtos mais similares ao primeiro item:")
st.table(similar_products)
