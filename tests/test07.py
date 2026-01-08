import streamlitrunner as sr
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def streamlit_charts():
    """Cria gráficos de linha, área e barras interativos"""
    x = np.linspace(0, 4 * np.pi, 40)
    sin = np.sin(x)
    cos = np.cos(x)
    df1 = pd.DataFrame({"x": x, "sin": sin, "cos": cos})
    st.header("Gráfico de linha")
    st.line_chart(df1, x="x")
    st.header("Gráfico de área")
    st.area_chart(df1, x="x")

    plats = ["P-10", "P-20", "P-30", "P-40"]
    counts = [10, 5, 3, 8]
    df2 = pd.DataFrame({"Contagem": counts, "UEP": plats})
    st.header("Gráfico de barras")
    st.bar_chart(df2, x="UEP")


def matplotlib_chart():
    """Cria gráfico estático do Matplotlib"""
    st.header("Usando Matplotlib")
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(np.arange(10), np.random.randint(0, 10, 10), "r")
    axes[1].scatter(np.arange(10), np.arange(10) ** 2)
    st.pyplot(fig)


def seaborn_chart():
    """Cria gráfico estático do Seaborn"""
    st.header("Usando Seaborn")
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    hist_data = np.hstack([x1, x2, x3])
    labels = 200 * ["Group 1"] + 200 * ["Group 2"] + 200 * ["Group 3"]
    fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    df = pd.DataFrame({"data": hist_data, "option": labels})
    sns.kdeplot(data=df, x="data", hue="option")
    st.pyplot(fig)


def main(a, b, c, d):
    st.title("7. Gráficos")
    np.random.seed(100)

    streamlit_charts()

    tab1, tab2 = st.tabs(["Usando Matplotlib", "Usando Seaborn"])
    with tab1:
        matplotlib_chart()
    with tab2:
        seaborn_chart()

    return a, b, c, d


if __name__ == "__main__":
    a = sr.run(main, [1, 2], {"c": 3, "d": 4}, screen=1, maximized=False)
    print(a)
