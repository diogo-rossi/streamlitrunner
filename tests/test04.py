import streamlitrunner as sr
import streamlit as st
import math


def select_box_input(valor: float):
    """Apresenta três opções de funções trigonométricas em uma select box

    Args:
        valor (float): o valor no qual será aplicada a função trigonométrica
    """
    st.header("Select box")
    opcoes = ["Seno", "Cosseno", "Tangente"]
    trig = st.selectbox("Qual função trigonométrica calcular?", opcoes)
    if trig == "Seno":
        st.text(f"O valor de sen({valor}) é f{math.sin(valor)}")
    elif trig == "Cosseno":
        st.text(f"O valor de cos({valor}) é f{math.cos(valor)}")
    else:
        st.text(f"O valor de tan({valor}) é f{math.tan(valor)}")


def checkbox_input(valor: float):
    """Apresenta um checkbox para definir se deve-se ou não calcular o quadrado
    do valor

    Args:
        valor (float): o valor que será elevado ao quadrado
    """
    st.header("Checkbox")
    quadrado = st.checkbox("Elevar ao quadrado?")
    if quadrado:
        st.text(f"O valor inicial de {valor} ao quadrado é {valor**2}")
    else:
        st.text(f"O valor inicial é {valor}")


def text_input(valor: float) -> float:
    """Apresenta uma caixa de texto para receber um valor numérico decimal

    Args:
        valor (float): o valor inicial para a caixa de texto

    Returns:
        float: o valor preenchido pelo usuário
    """
    st.header("Entrada de texto")
    valor = st.number_input("Qual o valor inicial?")
    st.text(f"{valor}")
    return valor


def main():
    st.title("4. Entrada de dados")
    valor = 0.0
    valor = text_input(valor)
    checkbox_input(valor)
    select_box_input(valor)


if __name__ == "__main__":
    main()
    sr.run(title="Input data", maximized=False)