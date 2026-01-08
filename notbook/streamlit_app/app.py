import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Analytics — Sales App", layout="wide")

BASE = Path(__file__).parent

st.title("📊 Sales Analytics — Data App")

# Carrega datasets automáticos
FILES = {
    "fact_sales": "fact_sales.csv",
    "dim_product": "dim_product.csv",
    "dim_categories": "dim_categories.csv",
    "dim_calendar": "dim_calendar.csv",
}

dfs = {}

for k, f in FILES.items():
    p = BASE / f
    if p.exists():
        dfs[k] = pd.read_csv(p)
    else:
        st.error(f"Arquivo não encontrado: {f}")

# Se não carregou tudo, para por aqui
if len(dfs) < 4:
    st.stop()

# Modelo Estrela (Join)
fact = dfs["fact_sales"]
dim_prod = dfs["dim_product"]
dim_cat = dfs["dim_categories"]
dim_cal = dfs["dim_calendar"]

df = fact.merge(dim_prod, on="product_id", how="left")
df = df.merge(dim_cat, on="category_id", how="left")
df = df.merge(dim_cal, on="date_id", how="left")

st.subheader("📁 Dados Integrados")
st.dataframe(df.head(), use_container_width=True)

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Revenue", f"{df['revenue'].sum():,.2f}")
col2.metric("🛒 Total Units", f"{df['quantity'].sum():,.0f}")
col3.metric("🎫 Ticket Médio", f"{(df['revenue'].sum()/df['quantity'].sum()):,.2f}")
col4.metric("📦 Produtos", df['product_id'].nunique())

# Filtros
st.sidebar.header("Filtros")

cats = st.sidebar.multiselect(
    "Categorias",
    sorted(df['category_name'].dropna().unique()),
    default=sorted(df['category_name'].dropna().unique())
)

df_f = df[df['category_name'].isin(cats)]

# Gráficos
tab1, tab2, tab3 = st.tabs(["📈 Time Series", "🏆 Top Produtos", "📂 Categorias"])

with tab1:
    time_col = "date" if "date" in df_f.columns else None
    if time_col:
        ts = df_f.groupby(time_col)['revenue'].sum().reset_index()
        fig = px.line(ts, x=time_col, y="revenue", title="Revenue Over Time")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    prod = df_f.groupby("product_name")['revenue'].sum().nlargest(10).reset_index()
    fig = px.bar(prod, x="product_name", y="revenue", title="Top Products")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    cat = df_f.groupby("category_name")['revenue'].sum().reset_index()
    fig = px.pie(cat, values="revenue", names="category_name", title="Share by Category")
    st.plotly_chart(fig, use_container_width=True)
