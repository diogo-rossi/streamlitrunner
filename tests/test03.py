import streamlitrunner as sr
import streamlit as st
import pandas as pd


def main():
    st.title("3. Tabelas")

    df = pd.DataFrame(
        {
            "Coluna 1": [1, 2, 3, 4],
            "Coluna 2": [10, 20, 30, 40],
            "Coluna 3": ["A", "B", "C", "D"],
        }
    )

    st.header("Tabela dinâmica")
    st.code("st.dataframe(df)")
    st.dataframe(df)

    st.header("Tabela estática")
    st.code("st.table(df)")
    st.table(df)


if __name__ == "__main__":
    main()
    sr.run()