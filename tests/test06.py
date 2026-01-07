import streamlitrunner as sr
import streamlit as st
import numpy as np


def create_buttons():
    """Cria os botões para adicionar número e limpar lista"""
    col1, col2 = st.columns(2)
    if col1.button("🎲 Adicionar número aleatório"):
        numero = np.random.randint(0, 100)
        st.session_state.lista.append(numero)

    if col2.button("🗑️ Limpar lista"):
        st.session_state.lista = []


def show_result():
    """Apresenta os resultados para o usuário"""
    st.header("Números aleatórios")
    st.write(st.session_state.lista)


def main():
    st.title("6. Persistência")

    if "lista" not in st.session_state:
        st.session_state.lista = []

    create_buttons()
    show_result()


if __name__ == "__main__":
    main()
    sr.run()
