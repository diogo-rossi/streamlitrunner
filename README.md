# Streamlit Runner

![](./docs/streamlitrunner.png)

A simple way to run Streamlit app as a desktop app

## Installation

```shell
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

![](docs/streamlitrunner-example.png)

## Documentation:

[https://streamlitrunner.readthedocs.io/en/latest/](https://streamlitrunner.readthedocs.io/en/latest/)
