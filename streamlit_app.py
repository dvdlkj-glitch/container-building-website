import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sabah Container Solutions",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Full-bleed layout: hide Streamlit chrome and remove page padding
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stVerticalBlock"] {gap: 0 !important;}
      iframe {display: block; border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

# The animated site is served by Streamlit's static file server
# (enableStaticServing = true in .streamlit/config.toml).
SITE_URL = "/app/static/animated-site/index.html"
DASHBOARD_URL = "/app/static/Container_Build_Dashboard_v2.html"

components.iframe(SITE_URL, height=950, scrolling=True)

st.markdown(
    f"""
    <div style="text-align:center; padding:14px; background:#0e0d0c; color:#c8c0b4;
                font-family:sans-serif; font-size:13px;">
      Best experienced full-screen:
      <a href="{SITE_URL}" target="_blank" style="color:#e8792b;">open the animated site</a>
      &nbsp;·&nbsp;
      <a href="{DASHBOARD_URL}" target="_blank" style="color:#e8792b;">open the build dashboard</a>
    </div>
    """,
    unsafe_allow_html=True,
)
