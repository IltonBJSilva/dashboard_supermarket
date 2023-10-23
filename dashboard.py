'''
Dashboard em python
Criado por: Ilton Batista
Data de inicio: 16/10/2023
Proposito: Desenvolver habilidades de raciocinio e experiencia com novas bibliotecas de analise de dados e dashboard




Perguntas a serem respondidas
 # Tudo com uma visão mensal
 - Faturamento por unidade.
 - Tipo de produto mais vendido, contribuição por filial.
 - Desempenho na forma de pagamento.
 - Como estão as avaliações das filias.

'''


import streamlit as st
import time
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv", sep=';', decimal=',') # leitura da base de dados
df["Date"] = pd.to_datetime(df["Date"]) # convert to datetime
df = df.sort_values(by="Date") # sort by date
df["Date"] = df["Date"].dt.date # removendo as horas de date

df['Month'] = df['Date'].apply(lambda x:str(x.year) + "-"+str(x.month)) # criando coluna de mes

month = st.sidebar.selectbox("Selecione o mês", df['Month'].unique()) # selecionando o mes

df_filtered = df[df["Month"] == month] # filtrando o mes

df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)


fig_date = px.bar(df_filtered, x="Date", y="Total", color="Branch", barmode="group", title="Faturamento por dia")

col1.plotly_chart(fig_date, use_container_width=True)



















