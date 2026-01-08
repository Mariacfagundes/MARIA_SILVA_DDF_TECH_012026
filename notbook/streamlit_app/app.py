# ============================================================
# ITEM 9 – DATA APP (Exploração com Streamlit)
# ============================================================

import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Carregar dados
products = pd.read_csv("AdventureWorks_Products.csv")
categories = pd.read_csv("AdventureWorks_Product_Categories.csv")

# Título do App
st.title("Exploração de Dados - AdventureWorks")

# Mostrar tabela de produtos
st.subheader("Produtos disponíveis")
st.dataframe(products.head())

# Receita média por categoria
st.subheader("Preço médio por categoria")
df_cat = products.merge(categories, left_on="ProductSubcategoryKey", right_on="ProductCategoryKey", how="left")
df_price_cat = df_cat.groupby("CategoryName")["ProductPrice"].mean().reset_index()
st.bar_chart(df_price_cat.set_index("CategoryName"))

# Similaridade entre produtos (usando descrição)
st.subheader("Similaridade entre produtos (descrição)")
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(products["ProductDescription"].fillna(""))

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Exemplo: mostrar os 5 produtos mais similares ao primeiro
similarities = list(enumerate(cosine_sim[0]))
similarities_sorted = sorted(similarities, key=lambda x: x[1], reverse=True)[1:6]
similar_products = products.iloc[[i[0] for i in similarities_sorted]][["ProductName", "ProductDescription"]]

st.write("Produtos mais similares ao primeiro item:")
st.table(similar_products)

