import streamlit as st
import sqlite3
import pandas as pd
import os
from datetime import date

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Prime Luxury Cars",
    page_icon="🏎️",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #0f0f0f, #000000);
    color: white;
}

[data-testid="stSidebar"] {
    background: #0a0a0a;
}

h1, h2, h3 {
    color: #D4AF37;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(135deg, #D4AF37, #FFD700);
    color: black;
    font-weight: bold;
    border-radius: 14px;
    height: 50px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# PATH BASE (IMAGENS FIX)
# =========================
BASE_DIR = os.path.dirname(__file__)

# =========================
# DATABASE
# =========================
conn = sqlite3.connect("reservas.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reservas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT,
    carro TEXT,
    retirada TEXT,
    devolucao TEXT,
    dias INTEGER,
    total REAL
)
""")
conn.commit()

# =========================
# CARROS
# =========================
carros = {
    "Lamborghini Aventador": 5000,
    "Ferrari 488 GTB": 5500,
    "Bugatti Chiron": 8000,
    "Aston Martin DB11": 4500,
    "Maserati MC20": 3500,
    "Jaguar F-Type": 2500,
    "Pagani Huayra": 9000,
    "Range Rover Sport": 2000
}

# =========================
# IMAGENS (SEGURAS)
# =========================
imagens = {
    "Lamborghini Aventador": os.path.join(BASE_DIR, "imagens", "lamborghini.jpg"),
    "Ferrari 488 GTB": os.path.join(BASE_DIR, "imagens", "ferrari.jpg"),
    "Bugatti Chiron": os.path.join(BASE_DIR, "imagens", "bugatti.jpg"),
    "Aston Martin DB11": os.path.join(BASE_DIR, "imagens", "aston.jpg"),
    "Maserati MC20": os.path.join(BASE_DIR, "imagens", "maserati.jpg"),
    "Jaguar F-Type": os.path.join(BASE_DIR, "imagens", "jaguar.jpg"),
    "Pagani Huayra": os.path.join(BASE_DIR, "imagens", "pagani.jpg"),
    "Range Rover Sport": os.path.join(BASE_DIR, "imagens", "range.jpg")
}

# =========================
# MENU
# =========================
st.sidebar.title("🏎️ Prime Luxury Cars")
pagina = st.sidebar.radio("Menu", ["Showroom", "Reserva", "Dashboard"])

# =========================
# SHOWROOM
# =========================
if pagina == "Showroom":
    st.title("🏁 Showroom Exclusivo")

    cols = st.columns(3)

    for i, (carro, preco) in enumerate(carros.items()):
        with cols[i % 3]:

            img = imagens.get(carro)

            if img and os.path.exists(img):
                st.image(img, use_container_width=True)
            else:
                st.warning("Imagem não encontrada")

            st.markdown(f"### {carro}")
            st.markdown(f"💰 R$ {preco:,.2f} / dia")

    st.info("Locação premium de supercarros.")

# =========================
# RESERVA
# =========================
elif pagina == "Reserva":
    st.title("📅 Nova Reserva")

    col1, col2 = st.columns([2, 1])

    with col1:
        carro = st.selectbox("Escolha o carro", list(carros.keys()))

        img = imagens.get(carro)
        if img and os.path.exists(img):
            st.image(img, use_container_width=True)

    with col2:
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")

        retirada = st.date_input("Retirada", date.today())
        devolucao = st.date_input("Devolução", date.today())

        dias = max((devolucao - retirada).days, 1)

        diaria = carros[carro]
        total = dias * diaria

        st.metric("Diária", f"R$ {diaria:,.2f}")
        st.metric("Dias", dias)
        st.metric("Total", f"R$ {total:,.2f}")

        if st.button("Confirmar Reserva 🚗"):

            if nome and email and telefone:

                cursor.execute("""
                INSERT INTO reservas (nome, email, telefone, carro, retirada, devolucao, dias, total)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (nome, email, telefone, carro, str(retirada), str(devolucao), dias, total))

                conn.commit()

                st.success("Reserva realizada com sucesso!")
                st.balloons()

            else:
                st.error("Preencha todos os campos")

# =========================
# DASHBOARD
# =========================
elif pagina == "Dashboard":
    st.title("📊 Painel Administrativo")

    dados = cursor.execute("SELECT * FROM reservas").fetchall()

    total = len(dados)
    faturamento = sum(d[8] for d in dados) if dados else 0
    media = faturamento / total if total else 0

    c1, c2, c3 = st.columns(3)
    c1.metric("Reservas", total)
    c2.metric("Faturamento", f"R$ {faturamento:,.2f}")
    c3.metric("Média", f"R$ {media:,.2f}")

    st.markdown("---")

    if dados:
        df = pd.DataFrame(dados, columns=[
            "ID", "Nome", "Email", "Telefone",
            "Carro", "Retirada", "Devolução",
            "Dias", "Total"
        ])
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("Nenhuma reserva ainda.")

# NÃO FECHAR CONEXÃO (streamlit recarrega o script)