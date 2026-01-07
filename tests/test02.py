import streamlitrunner as sr
import streamlit as st
import numpy as np


def section_1():
    """
    Cria a seção 1 da página usando apenas a função write do Streamlit
    """
    st.write("# Código usando Markdown")
    st.write("## Título nível 2")
    st.write("### Título nível 3")
    st.write("Texto normal")
    st.write("**Texto negrito**")
    st.write("_Texto itálico_")
    st.write(
        "```python\n"
        + "# Código python\n"
        + "import numpy as np\n"
        + "data = np.random.randint(0, 20, size=100)\n"
        + "```\n"
    )

    st.write(
        "Latex\n"
        + "- Inline: $E=mc^2$\n"
        + "- Bloco:\n"
        + "$$\n"
        + "\na + a\nr + a r^\n2 + a r^\n3 + \\cdot\ns + a r^{n-1} =\n"
        + "\\sum_{k=0}^{n-1} ar^k =\n"
        + "a \\left( \\frac{1-r^{n}}{1-r}\\right)\n"
        + "$$"
    )


def section_2():
    """
    Cria a seção 2 da página usando apenas funções específicas do Streamlit
    """
    st.title("Código usando funções")
    st.header("Título nível 2")
    st.subheader("Título nível 3")
    st.write("Texto normal")
    st.write("**Texto negrito**")
    st.write("_Texto itálico_")
    st.code(
        "# Código python\n"
        + "import numpy as np\n"
        + "data = np.random.randint(0, 20, size=100)\n",
        language="python",
    )
    st.latex(
        "a + ar + a r^2 + a r^3 + \\cdots + a r^{n-1} =\n"
        + "\\sum_{k=0}^{n-1} ar^k =\n"
        + "a \\left( \\frac{1-r^{n}}{1-r}\\right)"
    )


def main():
    st.write("# 2. Textos")
    section_1()
    section_2()


if __name__ == "__main__":
    main()
    sr.run(title="Texts", maximized=False)
