# ============================================================
# ITEM 9 – DATA APP (Exploração com Streamlit)
# ============================================================

import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Carregar dados (agora os arquivos estão na mesma pasta do app.py)
products = pd.read_csv("dim_product.csv")
categories = pd.read_csv("dim_categories.csv")
sales = pd.read_csv("fact_sales.csv")
calendar = pd.read_csv("dim_calendar.csv")

# Título do App
st.title("Exploração de Dados - AdventureWorks")

# Mostrar tabela de produtos
st.subheader("Produtos disponíveis")
st.dataframe(products.head())

# Preço médio por categoria
st.subheader("Preço médio por categoria")

# Ajuste de chaves: verifique os nomes reais das colunas nos CSVs
# Exemplo: se em dim_product.csv a coluna é "ProductCategoryKey"
# e em dim_categories.csv é "CategoryKey", ajuste abaixo:
df_cat = products.merge(
    categories,
    left_on="ProductCategoryKey",   # ajuste conforme o nome real da coluna
    right_on="CategoryKey",         # ajuste conforme o nome real da coluna
    how="left"
)

df_price_cat = df_cat.groupby("CategoryName")["ProductPrice"].mean().reset_index()
st.bar_chart(df_price_cat.set_index("CategoryName"))

# Similaridade entre produtos (usando descrição)
st.subheader("Similaridade entre produtos (descrição)")

# Se não houver coluna "ProductDescription", ajuste para a coluna correta
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(products["ProductDescription"].fillna(""))

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Exemplo: mostrar os 5 produtos mais similares ao primeiro
similarities = list(enumerate(cosine_sim[0]))
similarities_sorted = sorted(similarities, key=lambda x: x[1], reverse=True)[1:6]
similar_products = products.iloc[[i[0] for i in similarities_sorted]][["ProductName", "ProductDescription"]]

st.write("Produtos mais similares ao primeiro item:")
st.table(similar_products)
