import streamlitrunner as sr
import streamlit as st
import numpy as np


def main():
    st.write(
        """
    # My first app
    Hello World!
    """
    )

    data = np.random.randint(0, 20, size=100)
    st.line_chart(data)


if __name__ == "__main__":
    sr.run(title="My first app", maximized=False)
    main()
