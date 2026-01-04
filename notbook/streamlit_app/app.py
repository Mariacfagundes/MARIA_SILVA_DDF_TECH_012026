import streamlit as st
import pandas as pd

st.title("📊 AdventureWorks Data App")

# Carregar dados da camada analytics
dim_calendar = pd.read_csv("analytics/dim_calendar.csv")
dim_product = pd.read_csv("analytics/dim_product.csv")
dim_categories = pd.read_csv("analytics/dim_categories.csv")
fact_sales = pd.read_csv("analytics/fact_sales.csv")

# Filtros
st.sidebar.header("Filtros")
year_filter = st.sidebar.selectbox("Ano", sorted(dim_calendar["year"].unique()))
category_filter = st.sidebar.selectbox("Categoria", dim_categories["category_name"].unique())

# Preparar dados
df = fact_sales.merge(dim_product, on="product_key", how="left")
df = df.merge(dim_categories, left_on="product_key", right_on="category_key", how="left")
df = df.merge(dim_calendar, left_on="order_date", right_on="date", how="left")

# Aplicar filtros
df = df[(df["year"] == year_filter) & (df["category_name"] == category_filter)]

# KPIs
st.subheader("KPIs")
col1, col2 = st.columns(2)
col1.metric("Receita Total", f"${df['revenue'].sum():,.2f}")
col2.metric("Lucro Total", f"${df['profit'].sum():,.2f}")

# Receita mensal
st.subheader("Receita mensal")
df_month = df.groupby("month")["revenue"].sum().reset_index()
st.line_chart(df_month.set_index("month"))

# Top produtos
st.subheader("Top 10 produtos mais vendidos")
df_top = df.groupby("product_name")["order_quantity"].sum().reset_index().nlargest(10, "order_quantity")
st.bar_chart(df_top.set_index("product_name"))
