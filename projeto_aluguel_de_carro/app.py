import os
os.system("cls")

import streamlit as st
from datetime import datetime

st.sidebar.image("logo.svg")
st.sidebar.title("Locadora De Carros🚗")

carro = st.sidebar.selectbox("Selecione o carro que Deseja alugar",
                              ["Lamborghini","Aston Martin","Ferrari","Jaguar","Bugatti","Maserati","Pagani","Land Rover" ])

valores_diarias = {"Lamborghini": 5000,"Aston Martin": 4500, "Ferrari": 5500,"Jaguar": 2500,"Bugatti": 8000,"Maserati": 3500,"Pagani": 9000,"Land Rover": 2000}
valor_diaria = valores_diarias[carro]
st.image(f"{carro}.png")
st.subheader(f"{carro} - Diaria: R$ {valores_diarias[carro]}")

data_retirada = st.date_input("Selecione o Dia da Retirada:",datetime.now(),datetime.now())
data_devolucao = st.date_input("Selecione o Dia da Devolução:",data_retirada,data_retirada)

if st.button("Alugar"):
    dias= (data_devolucao - data_retirada).days
    valor_total = valor_diaria * dias
    st.write(f"Carro escolhido **{carro}**")
    st.metric("Total do aluguel", f"R$ {valor_total:.2f}")
    