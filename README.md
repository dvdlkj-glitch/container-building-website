# Sabah Container Solutions — Animated Website

A cinematic scroll-driven website for a container building business in Kota Kinabalu, Sabah.
Scrolling plays a construction-site video frame-by-frame (112 WebP frames on canvas) while
six content sections fade in: hero, vision, build-anatomy detail callouts, catalog groups A–F,
build timeline, and a call-to-action that opens the companion sales/estimate dashboard.

## Structure

```
streamlit_app.py                  # Streamlit wrapper (embeds the site full-bleed)
.streamlit/config.toml            # enableStaticServing = true
static/
├── animated-site/
│   ├── index.html                # the scroll-animated website (single file)
│   └── frames/                   # desktop (1920x1080) + mobile (960x540) WebP frames
├── Container_Build_Dashboard_v2.html   # sales, estimate & build-tracking dashboard
└── dashboard_assets/             # dashboard images
```

## Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and pick this repo.
2. Main file: `streamlit_app.py`. Deploy.
3. The animated site is served at `<your-app-url>/app/static/animated-site/index.html`
   (the app embeds it and also links to the full-screen version).

## Run locally

```
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Or serve the static site directly without Streamlit:

```
python -m http.server 8080 --directory static
# then open http://localhost:8080/animated-site/index.html
```
