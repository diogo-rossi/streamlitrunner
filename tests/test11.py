import numpy as np
import streamlitrunner as sr
import streamlit as st
from plotly.graph_objects import Figure, Scatter, Layout
from plotly.subplots import make_subplots

x = np.linspace(0, 10, 1000)
y = np.sin(x)

fig = make_subplots().add_trace(Scatter(x=x, y=np.sin(x)))

sr.show_plotly_fig(fig, matplotlib_layout=True)
