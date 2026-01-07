import streamlit as st
import streamlitrunner as sr

class Well:
    def __init__(self, name: str, lda: float, uep: str, objective: str):
        self.name = name
        self.lda = lda
        self.uep = uep
        self.objective = objective


def build_sidebar(data: dict) -> str:
    """Constrói a sidebar

    Args:
        data (dict): um dicionário de dados de poços indexado pelo nome dos
        poços

    Returns:
        str: o texto da opção salecionada
    """
    st.sidebar.title("Sidebar")
    poco = st.sidebar.radio(
        "Qual o poço?", [nome_poco for nome_poco in data] + ["Todos"]
    )
    return poco


def build_main(poco: Well):
    """Constrói a seção principal com os dados do poço selecionado

    Args:
        poco (Well): objeto poço que foi selecionado na sidebar
    """
    columns = st.columns(2)
    columns[0].write("**Poço**")
    columns[0].write("**LDA (m)**")
    columns[0].write("**Unidade de Produção**")
    columns[0].write("**Objetivo**")
    columns[1].write(f"{poco.name}")
    columns[1].write(f"{poco.lda:.0f}")
    columns[1].write(f"{poco.uep}")
    columns[1].write(f"{poco.objective}")


def build_tabs(data: dict):
    """Constrói seção de abas

    Args:
        data (dict): um dicionário de dados de poços indexado pelo nome dos
        poços
    """
    tabs = st.tabs(data)
    for poco, tab in zip(data, tabs):
        tab.write(f"**Poço**: {data[poco].name}")
        tab.write(f"**LDA (m)**: {data[poco].lda:.0f}")
        tab.write(f"**Unidade de Produção**: {data[poco].uep}")
        tab.write(f"**Objetivo**: {data[poco].objective}")


def main():
    data = {
        "BUZ-10": Well("BUZ-10", 2058, "P-75", "Produção"),
        "BUZ-11": Well("BUZ-11", 1977, "Não interligado", "N/D"),
        "BUZ-12": Well("BUZ-12", 2037, "P-77", "Produção"),
        "BUZ-17": Well("BUZ-17", 2043, "P-74", "Produção"),
    }
    st.title("5. Estrutura")
    nome_poco = build_sidebar(data)
    if nome_poco != "Todos":
        build_main(data[nome_poco])
    else:
        build_tabs(data)


if __name__ == "__main__":
    sr.run(maximized=False)
    main()
