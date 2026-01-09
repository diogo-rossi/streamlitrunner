import numpy as np
import streamlitrunner as sr
import streamlit as st
from plotly.graph_objects import Figure, Scatter, Layout
from plotly.subplots import make_subplots

x = np.linspace(0, 100, 1000)
y = np.sin(x)
# scatter: Scatter = Scatter(x=x, y=y)
layout: Layout = Layout(
    template="simple_white",
    plot_bgcolor="white",
    height=500,
    margin=dict(l=50, r=0, t=30, b=0),
)
fig = (
    make_subplots(2, 2)
    .update_layout(layout)
    .update_xaxes(mirror="allticks", ticks="inside", showgrid=True)
    .update_yaxes(mirror="allticks", ticks="inside", showgrid=True)
    .add_trace(Scatter(x=x, y=np.sin(x)), 1, 1)
    .add_trace(Scatter(x=x, y=np.cos(x)), 1, 2)
    .add_trace(Scatter(x=x, y=np.sin(2 * x)), 2, 1)
    .add_trace(Scatter(x=x, y=np.cos(2 * x)), 2, 2)
)

sr.show_plotly_fig(fig)
