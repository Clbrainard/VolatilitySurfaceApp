
import os
from ivSurface import IvSurface
import streamlit as st
import plotly.graph_objects as go 
import math

KEY="HB7ZSa2dZbO5DjohKM7L3ll4JtpX1cZH"

def plot(ticker):
    surface = IvSurface(ticker,KEY)
    plt = surface.get_plot()
    plt.update_layout(
        height=800,   # try 700–900 px depending on preference
        width=1100   # optional
    )
    return plt


# Assumes this exists elsewhere in your project:
# from my_module import plot  # plot(ticker: str) -> plotly.graph_objs.Figure

st.set_page_config(page_title="Volatility surface visualizer", layout="wide")

st.title("Volatility Surface visualizer")

# ----- Sidebar -----
st.sidebar.header("Inputs")
ticker = st.sidebar.text_input("Ticker", value="AAPL").strip()
render = st.sidebar.button("Render")

# ----- Main Area -----
placeholder = st.empty()

if render:
    if not ticker:
        st.warning("Please enter a ticker symbol.")
    else:
        try:
            with st.spinner(f"Rendering surface for {ticker.upper()}..."):
                fig = plot(ticker.upper())   # <- your prewritten function
            # Render the Plotly figure
            placeholder.plotly_chart(fig, use_container_width=True)
            fig.update_layout(height=800)
        except Exception as e:
            st.error(f"Failed to render plot for '{ticker}': {e}")
else:
    st.caption("Enter a ticker in the sidebar and click **Render** to display the 3D chart.")
