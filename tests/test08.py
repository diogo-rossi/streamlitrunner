import numpy as np
import streamlitrunner as sr
import streamlit as st
from plotly.graph_objects import Figure, Scatter, Layout

x = np.linspace(0, 10, 100)
y = np.sin(x)
scatter: Scatter = Scatter(x=x, y=y)
layout: Layout = Layout(
    template="simple_white",
    plot_bgcolor="white",
    height=500,
    margin=dict(l=50, r=40, t=30, b=0),
)
fig = (
    Figure(layout=layout)
    .add_trace(trace=scatter)
    .update_xaxes(mirror="allticks", ticks="inside", showgrid=True)
    .update_yaxes(mirror="allticks", ticks="inside", showgrid=True)
)
sr.show_plotly_fig(fig)
