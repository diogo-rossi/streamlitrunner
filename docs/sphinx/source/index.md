# Streamlit-Runner

A simple way to run Streamlit app as a desktop app

## Installation

```bash
pip install streamlitrunner
```

## Usage

Import `streamlitrunner` and call `run()`

```python
# my_app.py
import streamlitrunner as sr
import streamlit as st

st.title("Hello World!")
st.write("This is a simple text example.")

if __name__ == '__main__':
    sr.run()
```

Now you can only call `python my_app.py` and it will work as a desktop app!

![](../../streamlitrunner-example.png)

## Links

```{toctree}
:maxdepth: 1
API_reference
```

- GitHub repository:
  [https://github.com/diogo-rossi/streamlitrunner](https://github.com/diogo-rossi/streamlitrunner)
- PyPI:
  [https://pypi.org/project/streamlitrunner/](https://pypi.org/project/streamlitrunner/)
- Documentation:
  [https://streamlitrunner.readthedocs.io/en/latest/](https://streamlitrunner.readthedocs.io/en/latest/)
