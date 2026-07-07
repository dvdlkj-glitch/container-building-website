import streamlit as st

st.set_page_config(
    page_title="Sabah Container Solutions",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit Community Cloud's proxy currently breaks /app/static file serving
# (their own static-file-serving demo app is broken the same way), so the
# static site is hosted on GitHub Pages and embedded here.
PAGES_BASE = "https://dvdlkj-glitch.github.io/container-building-website"
SITE_URL = f"{PAGES_BASE}/static/animated-site/index.html"
DASHBOARD_URL = f"{PAGES_BASE}/static/Container_Build_Dashboard_v2.html"

st.markdown(
    f"""
    <style>
      #MainMenu, header, footer {{visibility: hidden;}}
      .stApp {{background: #0e0d0c;}}
      .block-container {{padding: 0 !important; max-width: 100% !important;}}
      [data-testid="stVerticalBlock"] {{gap: 0 !important;}}
    </style>
    <iframe src="{SITE_URL}"
            style="width:100%; height:94vh; border:none; display:block; background:#0e0d0c;"
            allow="fullscreen"></iframe>
    <div style="text-align:center; padding:12px; background:#0e0d0c; color:#c8c0b4;
                font-family:sans-serif; font-size:13px;">
      Best experienced full-screen:
      <a href="{SITE_URL}" target="_blank" style="color:#e8792b;">open the animated site</a>
      &nbsp;·&nbsp;
      <a href="{DASHBOARD_URL}" target="_blank" style="color:#e8792b;">open the build dashboard</a>
    </div>
    """,
    unsafe_allow_html=True,
)
