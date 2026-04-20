# src/app.py
import streamlit as st
from agente import perguntar_edu

st.set_page_config(
    page_title="EDU — Educador Financeiro",
    page_icon="📚",
    layout="centered"
)

st.title("📚 EDU — Seu Educador Financeiro")
st.caption("Tire dúvidas sobre suas finanças com base nos seus dados reais.")

# Inicializa o histórico de conversa
if "historico" not in st.session_state:
    st.session_state.historico = []

# Botão para limpar conversa
if st.button("🗑️ Limpar conversa"):
    st.session_state.historico = []
    st.rerun()

# Exibe as mensagens anteriores
for msg in st.session_state.historico:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Campo de input do usuário
pergunta = st.chat_input("Digite sua pergunta financeira...")

if pergunta:
    # Mostra a mensagem do usuário
    with st.chat_message("user"):
        st.write(pergunta)

    st.session_state.historico.append({
        "role": "user",
        "content": pergunta
    })

    # Gera e mostra a resposta do EDU
    with st.chat_message("assistant"):
        with st.spinner("EDU está consultando sua base de dados..."):
            try:
                resposta = perguntar_edu(pergunta, st.session_state.historico)
                st.write(resposta)
                st.session_state.historico.append({
                    "role": "assistant",
                    "content": resposta
                })
            except Exception as e:
                st.error(f"Erro ao consultar o EDU: {e}")