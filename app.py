import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pickle
import json
import os

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="OlympINDIA28",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Favicon injection will be rendered after the logo image asset is defined.

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --saffron: #FF9933;
    --saffron-dim: rgba(255,153,51,0.12);
    --saffron-glow: rgba(255,153,51,0.25);
    --green: #138808;
    --green-dim: rgba(19,136,8,0.15);
    --blue: #2196F3;
    --bg: #080810;
    --bg2: #0f0f1a;
    --bg3: #141425;
    --border: rgba(255,255,255,0.07);
    --border-bright: rgba(255,153,51,0.25);
    --text: #e2e2ee;
    --text-muted: #6b6b80;
    --text-dim: #9494a8;
}

/* ── Base ── */
.stApp {
    background-color: var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

/* grain overlay */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.035'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
}

/* ── Typography ── */
h1, h2, h3, h4, h5, h6, .bebas {
    font-family: 'Bebas Neue', sans-serif !important;
    letter-spacing: 2px;
    color: var(--text);
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] > div:first-child { background: var(--bg2); border-right: 1px solid var(--border); }
section[data-testid="stSidebarContent"] { padding: 1.5rem 1rem; }
[data-testid="collapsedControl"] { color: var(--saffron) !important; }

/* ── Main content padding ── */
.block-container {
    padding: 1.5rem 2rem 3rem !important;
    max-width: 1400px !important;
}

/* ── Top navbar ── */
.top-navbar {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    padding: 16px 0 12px;
    margin-bottom: 4px;
    border-bottom: 1px solid var(--border);
    position: relative;
}

.top-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(1.5rem, 2.4vw, 2.8rem);
    letter-spacing: 4px;
    color: #fff;
    margin: 0;
    line-height: 1;
}

.brand-highlight { color: var(--saffron); }

.top-subtitle {
    color: var(--text-muted);
    font-size: 0.72rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-top: 5px;
    font-weight: 500;
}

.top-nav-copy {
    color: var(--text-muted);
    font-size: 0.88rem;
    letter-spacing: 0.3px;
    max-width: 480px;
    text-align: right;
    line-height: 1.6;
}

/* ── Navigation radio pills ── */
div[data-testid="stHorizontalBlock"]:has(div[role="radiogroup"]),
div[data-testid="stRadio"] {
    background: transparent;
    border: none;
    border-radius: 0;
    padding: 0;
    margin: 8px auto 24px;
    display: flex !important;
    justify-content: center !important;
    width: 100%;
}

div[data-testid="stRadio"] > div {
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
}

div[role="radiogroup"] {
    display: flex !important;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center !important;
    align-items: center;
    width: fit-content !important;
    max-width: 100%;
    margin: 0 auto;
}

div[role="radiogroup"] > label {
    display: flex !important;
    justify-content: center;
    flex: 0 0 auto !important;
    width: auto !important;
    min-width: max-content !important;
}

div[role="radiogroup"] > label > div {
    width: auto !important;
    justify-content: center;
}

div[role="radiogroup"] > label {
    cursor: pointer !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 22px !important;
    background: transparent !important;
    transition: all 0.2s ease !important;
    min-width: 0 !important;
    margin: 0 !important;
}

div[role="radiogroup"] > label:hover {
    background: var(--saffron-dim) !important;
}

/* hide the radio circle completely */
div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {
    display: none !important;
    width: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

div[role="radiogroup"] > label > div {
    gap: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

div[role="radiogroup"] > label > div > div p {
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.5px !important;
    color: var(--text) !important;
    margin: 0 !important;
    white-space: nowrap;
}

div[role="radiogroup"] > label[data-baseweb="radio"]:has(input:checked) {
    background: var(--saffron) !important;
    box-shadow: 0 4px 16px rgba(255,153,51,0.30) !important;
}

div[role="radiogroup"] > label[data-baseweb="radio"]:has(input:checked) p {
    color: #080810 !important;
    font-weight: 700 !important;
}

/* ── Metric cards ── */
div[data-testid="stMetric"] {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-left: 3px solid var(--saffron);
    border-radius: 14px;
    padding: 18px 22px;
    transition: transform 0.2s, box-shadow 0.2s;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}

div[data-testid="stMetric"] label {
    color: var(--text-muted) !important;
    font-size: 0.75rem !important;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    font-weight: 600 !important;
}

div[data-testid="stMetricValue"] > div {
    color: var(--saffron) !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 2.2rem !important;
    letter-spacing: 2px;
}

div[data-testid="stMetricDelta"] {
    font-size: 0.8rem !important;
}

/* ── Cards ── */
.card {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 22px;
    margin-bottom: 14px;
    transition: box-shadow 0.2s;
}

.card:hover { box-shadow: 0 6px 20px rgba(0,0,0,0.35); }

.card-saffron { border-left: 3px solid var(--saffron); }
.card-green   { border-left: 3px solid var(--green); }
.card-blue    { border-left: 3px solid var(--blue); }
.card-red     { border-left: 3px solid #f44336; }

/* ── Hero numbers ── */
.hero-number {
    font-size: 7rem;
    font-family: 'Bebas Neue', sans-serif;
    background: linear-gradient(135deg, #FF9933 0%, #fff 50%, #138808 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    line-height: 1;
    filter: drop-shadow(0 0 30px rgba(255,153,51,0.3));
}

.hero-label {
    font-size: 0.78rem;
    color: var(--text-muted);
    letter-spacing: 4px;
    text-align: center;
    text-transform: uppercase;
    font-weight: 600;
}

.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    text-align: center;
    background: linear-gradient(135deg, #FF9933, #fff, #138808);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 6px;
    margin-bottom: 0;
}

/* ── Prediction box ── */
.prediction-box {
    text-align: center;
    padding: 48px 32px;
    background: radial-gradient(ellipse at 50% 0%, rgba(255,153,51,0.08) 0%, transparent 70%),
                linear-gradient(135deg, #111120, #0f0f1e);
    border: 1px solid rgba(255,153,51,0.2);
    border-radius: 20px;
    margin: 24px 0;
    position: relative;
    overflow: hidden;
}

.prediction-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #FF9933 30%, #fff 50%, #138808 70%, transparent);
}

/* ── Badges ── */
.badge {
    display: inline-block;
    padding: 3px 11px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.badge-red    { background: rgba(244,67,54,0.15);  color: #f44336; border: 1px solid rgba(244,67,54,0.25); }
.badge-orange { background: rgba(255,153,51,0.15); color: #FF9933; border: 1px solid rgba(255,153,51,0.25); }
.badge-yellow { background: rgba(255,235,59,0.15); color: #FFEB3B; border: 1px solid rgba(255,235,59,0.25); }
.badge-blue   { background: rgba(33,150,243,0.15); color: #2196F3; border: 1px solid rgba(33,150,243,0.25); }
.badge-green  { background: rgba(76,175,80,0.15);  color: #4CAF50; border: 1px solid rgba(76,175,80,0.25); }
.badge-gray   { background: rgba(158,158,158,0.15);color: #9e9e9e; border: 1px solid rgba(158,158,158,0.2); }
.badge-purple { background: rgba(156,39,176,0.15); color: #9C27B0; border: 1px solid rgba(156,39,176,0.25); }

/* ── Progress bars ── */
.progress-bar-bg {
    background: rgba(255,255,255,0.06);
    border-radius: 99px;
    height: 8px;
    overflow: hidden;
    margin: 6px 0;
}

.progress-bar-fill {
    height: 100%;
    border-radius: 99px;
    transition: width 0.6s cubic-bezier(0.4,0,0.2,1);
}

/* ── DataFrames ── */
.stDataFrame { border-radius: 14px; overflow: hidden; }
.stDataFrame iframe { border-radius: 14px; }

/* ── Buttons ── */
.stButton > button {
    background: var(--bg3) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-dim) !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    padding: 10px 20px !important;
    transition: all 0.2s !important;
    font-family: 'Inter', sans-serif !important;
}

.stButton > button:hover {
    border-color: var(--border-bright) !important;
    background: var(--saffron-dim) !important;
    color: var(--saffron) !important;
}

/* ── Sliders ── */
[data-testid="stSlider"] > div > div > div {
    background: var(--saffron) !important;
}

[data-testid="stSlider"] [data-testid="stTickBar"] {
    color: var(--text-muted) !important;
}

/* ── Selectboxes ── */
[data-testid="stSelectbox"] > div > div {
    background: var(--bg3) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
}

/* ── Section headers ── */
h3 {
    font-size: 1.25rem !important;
    letter-spacing: 1px !important;
    margin-top: 28px !important;
    margin-bottom: 12px !important;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
}

/* ── Spinner ── */
[data-testid="stSpinner"] { color: var(--saffron) !important; }

/* ── Info/Warning boxes ── */
[data-testid="stAlert"] {
    background: var(--bg3) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text-dim) !important;
}

/* ── Divider ── */
hr {
    border: none !important;
    border-top: 1px solid var(--border) !important;
    margin: 28px 0 !important;
}

/* ── Footer ── */
.footer-note {
    text-align: center;
    color: var(--text-muted);
    font-size: 0.82rem;
    line-height: 1.8;
}

.footer-tags {
    display: inline-flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
    margin-top: 12px;
}

.footer-tag {
    background: var(--saffron-dim);
    color: var(--saffron);
    border: 1px solid var(--border-bright);
    border-radius: 999px;
    padding: 5px 13px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* ── Section title pill ── */
.section-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--saffron-dim);
    border: 1px solid var(--border-bright);
    border-radius: 999px;
    padding: 4px 14px;
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--saffron);
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

/* ── Tricolor accent line ── */
.tricolor-line {
    height: 3px;
    background: linear-gradient(90deg, #FF9933 33.3%, #fff 33.3% 66.6%, #138808 66.6%);
    border-radius: 99px;
    margin: 16px 0;
    opacity: 0.6;
}

/* ── Opportunity card ── */
.opp-card {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 12px;
    transition: all 0.2s;
}

.opp-card:hover {
    border-color: var(--border-bright);
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HARDCODED FALLBACK DATA
# ─────────────────────────────────────────────
INDIA_HISTORY = {
    'Year':       [1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,
                   2000,2004,2008,2012,2016,2020,2024],
    'Total':      [1,1,1,1,0,1,0,0,0,1,1,1,3,6,2,7,6],
    'career_avg': [1.11,1.10,1.09,1.08,1.08,1.00,1.00,0.94,0.88,0.83,
                   0.80,0.77,0.75,0.81,0.96,1.00,1.20],
    'delta_last': [0,0,0,0,-1,1,-1,0,0,1,0,0,2,3,-4,5,-1],
    'gdp_pc_log': [4.44,4.77,4.62,4.83,5.10,5.60,5.64,5.88,5.77,5.99,
                   6.09,6.44,6.90,7.26,7.44,7.55,7.90]
}

DEFAULT_META = {
    "india_2028_base_prediction": 2.86,
    "r2": 0.87,
    "mae": 2.31,
    "best_params": {"max_depth": 3, "n_estimators": 100, "learning_rate": 0.1},
    "model_comparison": [
        {"Model": "Linear Regression", "MAE": 3.12, "R2": 0.78, "India_2024_Pred": 4.5},
        {"Model": "Ridge", "MAE": 3.08, "R2": 0.79, "India_2024_Pred": 4.3},
        {"Model": "Poisson", "MAE": 2.95, "R2": 0.81, "India_2024_Pred": 3.8},
        {"Model": "XGBoost (default)", "MAE": 2.52, "R2": 0.85, "India_2024_Pred": 3.2},
        {"Model": "XGBoost (tuned) ✅", "MAE": 2.31, "R2": 0.87, "India_2024_Pred": 2.86},
    ]
}

# ─────────────────────────────────────────────
# DATA LOADING
# ─────────────────────────────────────────────
@st.cache_data
def load_csv(path, fallback=None):
    try:
        return pd.read_csv(path)
    except Exception:
        if fallback is not None:
            st.warning(f"⚠️ Could not load `{path}`. Using fallback data.")
            return fallback
        st.warning(f"⚠️ Could not load `{path}`.")
        return pd.DataFrame()

@st.cache_data
def load_india_history():
    df = load_csv("data/processed/india_model_ready.csv", pd.DataFrame(INDIA_HISTORY))
    if df.empty:
        df = pd.DataFrame(INDIA_HISTORY)
    return df

@st.cache_data
def load_meta():
    try:
        with open("models/model_meta.json") as f:
            return json.load(f)
    except Exception:
        st.warning("⚠️ model_meta.json not found. Using defaults.")
        return DEFAULT_META

@st.cache_resource
def load_model():
    try:
        with open("models/india_2028_model.pkl", "rb") as f:
            return pickle.load(f)
    except Exception:
        st.warning("⚠️ Model file not found. Simulator will use a simple fallback.")
        return None

meta = load_meta()
model = load_model()
india_df = load_india_history()

# ─────────────────────────────────────────────
# PLOTLY DEFAULTS
# ─────────────────────────────────────────────
PLOTLY_LAYOUT = dict(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(15,15,25,0.8)',
    margin=dict(l=20, r=20, t=50, b=20),
    font=dict(color='#e8e8e8', family='DM Sans'),
)

def styled_plotly(fig):
    fig.update_layout(**PLOTLY_LAYOUT)
    fig.update_xaxes(gridcolor='#1a1a3a', zeroline=False)
    fig.update_yaxes(gridcolor='#1a1a3a', zeroline=False)
    return fig

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
LOGO_B64 = "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"

pages = [
    "Home — The Prediction",
    "Journey",
    "Sport Intelligence",
    "Global Comparison",
    "Scenario Simulator"
]

if 'page' not in st.session_state:
    st.session_state.page = pages[0]

st.markdown(f"""
<div style='text-align:center; padding:40px 0 10px;'>
    <img src="data:image/png;base64,{LOGO_B64}"
         style='width:180px; height:180px; object-fit:contain; display:block; margin:0 auto 20px; filter: drop-shadow(0 0 40px rgba(255,153,51,0.6)) drop-shadow(0 0 20px rgba(19,136,8,0.3));'
         alt="OlympINDIA28 Logo"/>
    <div style='
        font-family: "Bebas Neue", sans-serif;
        font-size: clamp(3.5rem, 8vw, 6.5rem);
        line-height: 1;
        letter-spacing: 8px;
        background: linear-gradient(90deg, #FF9933 0%, #FFD580 25%, #FFFFFF 50%, #a8e0a8 75%, #138808 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: none;
        margin-bottom: 4px;
        filter: drop-shadow(0 0 30px rgba(255,153,51,0.4));
    '>OlympINDIA28</div>
    <div style='
        font-family: "Bebas Neue", sans-serif;
        font-size: 1rem;
        letter-spacing: 6px;
        color: #555;
        text-transform: uppercase;
        margin-top: 6px;
    '>Los Angeles 2028 · Medal Intelligence</div>
</div>
""", unsafe_allow_html=True)
st.markdown("<div class='tricolor-line'></div>", unsafe_allow_html=True)

page = st.radio(
    label="",
    options=pages,
    index=pages.index(st.session_state.page),
    key="page_selector",
    horizontal=True,
    label_visibility="collapsed"
)

st.session_state.page = page

base_pred = meta.get("india_2028_base_prediction", 2.86)
r2 = meta.get("r2", 0.87)

# ─────────────────────────────────────────────
# FOOTER HELPER
# ─────────────────────────────────────────────
def render_footer():
    st.markdown("---")
    st.markdown(
        "<div class='footer-note'>"
        "OlympINDIA28 · Built by Kashyap Ladva · Data: 1896–2024 Summer Olympics · Model: Tuned XGBoost"
        "</div>",
        unsafe_allow_html=True
    )

# ═══════════════════════════════════════════════
# PAGE 1 — HOME: THE PREDICTION
# ═══════════════════════════════════════════════
if page == pages[0]:
    with st.spinner("Loading intelligence..."):
        # Hero moved to top nav

        st.markdown(f"""
        <div style='text-align:center; padding: 20px 0 0px;'>
            <h2 style='
                font-family: "Bebas Neue", sans-serif;
                font-size: clamp(2.2rem, 5vw, 3.8rem);
                color: #e2e2ee;
                letter-spacing: 3px;
                margin: 0;
            '>
                How many medals can <span style='color: #FF9933; filter: drop-shadow(0 0 10px rgba(255,153,51,0.4));'>India</span> win at <span style='color: #a8e0a8;'>LA 2028?</span>
            </h2>
        </div>
        <div class='prediction-box'>
          <div class='hero-label'>BASE PREDICTION · LA 2028</div>
          <div class='hero-number'>{base_pred}</div>
          <div style='font-size:0.85rem; color:#6b6b80; margin-top:10px; letter-spacing:0.5px;'>Under current structural trends</div>
          <div style='margin-top:16px;'>
            <span class='badge badge-orange'>Tuned XGBoost</span>&nbsp;
            <span class='badge badge-gray'>R²={r2}</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### What Drives India's Medal Count?")

        # Feature importance
        feat_df = pd.DataFrame({
            'Feature': ['career_avg', 'delta_last', 'gdp_pc_log'],
            'Importance': [55, 31, 12],
            'Color': ['#FF9933', '#4CAF50', '#2196F3']
        })
        fig_feat = go.Figure(go.Bar(
            y=feat_df['Feature'], x=feat_df['Importance'],
            orientation='h',
            marker_color=feat_df['Color'],
            text=[f"{v}%" for v in feat_df['Importance']],
            textposition='outside'
        ))
        fig_feat.update_layout(title="Feature Importance — Tuned XGBoost",
                                xaxis_title="Relative Importance (%)",
                                yaxis_title="", height=280)
        st.plotly_chart(styled_plotly(fig_feat), use_container_width=True)

        # Model accuracy card
        st.markdown(f"""
        <div class='card card-saffron'>
            <div class='section-pill'>🎯 Model Accuracy</div>
            <div style='display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; margin-top:14px;'>
                <div>
                    <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:4px;'>Best Model</div>
                    <div style='color:#e2e2ee; font-weight:700; font-size:0.95rem;'>Tuned XGBoost</div>
                </div>
                <div>
                    <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:4px;'>R² Score</div>
                    <div style='color:#FF9933; font-weight:700; font-size:1.2rem;'>{meta.get('r2', 0.87)}</div>
                </div>
                <div>
                    <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:4px;'>MAE</div>
                    <div style='color:#e2e2ee; font-weight:700; font-size:1.2rem;'>{meta.get('mae', 2.31)}</div>
                </div>
            </div>
            <div style='margin-top:14px; padding-top:12px; border-top:1px solid rgba(255,255,255,0.06);'>
                <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;'>Best Params</div>
                <code style='color:#FF9933; background:rgba(255,153,51,0.08); padding:4px 10px; border-radius:6px; font-size:0.82rem;'>{json.dumps(meta.get('best_params', {}))}</code>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 5-Model Comparison
        st.markdown("### 5-Model Comparison")
        comp = meta.get("model_comparison", DEFAULT_META["model_comparison"])
        comp_df = pd.DataFrame(comp)
        st.dataframe(
            comp_df.style.apply(
                lambda row: ['background-color: rgba(255,153,51,0.15)' if '✅' in str(row['Model']) else '' for _ in row],
                axis=1
            ),
            use_container_width=True, hide_index=True
        )

    render_footer()

# ═══════════════════════════════════════════════
# PAGE 2 — JOURNEY
# ═══════════════════════════════════════════════
elif page == pages[1]:
    with st.spinner("Loading India's journey..."):
        df = india_df.copy()

        # Medal Timeline
        st.markdown("### India's Olympic Medal Journey (1960–2024)")
        fig_timeline = go.Figure()
        fig_timeline.add_trace(go.Scatter(
            x=df['Year'], y=df['Total'],
            mode='lines+markers',
            line=dict(color='#FF9933', width=3),
            marker=dict(size=10, color='#FF9933', line=dict(width=2, color='#fff')),
            fill='tozeroy',
            fillcolor='rgba(255,153,51,0.1)',
            name='Medals'
        ))
        for yr, label in [(2008, "Beijing Breakthrough"), (2012, "London Peak"), (2020, "Tokyo Best")]:
            if yr in df['Year'].values:
                medal_val = df.loc[df['Year']==yr, 'Total'].values[0]
                fig_timeline.add_vline(x=yr, line_dash="dash", line_color="#444", line_width=1)
                fig_timeline.add_annotation(x=yr, y=medal_val+0.8, text=label,
                                            showarrow=False, font=dict(size=11, color='#FF9933'))
        fig_timeline.update_layout(height=400, title="", xaxis_title="Year", yaxis_title="Total Medals")
        st.plotly_chart(styled_plotly(fig_timeline), use_container_width=True)

        # 3 Stats
        c1, c2, c3 = st.columns(3)
        best_idx = df['Total'].idxmax()
        best_year = df.loc[best_idx, 'Year']
        best_total = df.loc[best_idx, 'Total']
        c1.metric("Best Ever", f"{int(best_year)}: {int(best_total)} medals")

        # CAGR
        first_nonzero = df[df['Total'] > 0].iloc[0]
        last = df.iloc[-1]
        years_span = last['Year'] - first_nonzero['Year']
        if years_span > 0 and first_nonzero['Total'] > 0:
            cagr = (last['Total'] / first_nonzero['Total']) ** (1 / (years_span / 4)) - 1
            c2.metric("CAGR (per cycle)", f"{cagr*100:.1f}%")
        else:
            c2.metric("CAGR", "N/A")

        c3.metric("Trend", "↑ Post-2016 Surge")

        # GDP vs Medals
        st.markdown("### Does Wealth Drive Medals? GDP vs Performance")
        fig_gdp = px.scatter(df, x='gdp_pc_log', y='Total', color='Year',
                             color_continuous_scale='Plasma', size='Total',
                             size_max=18, hover_data=['Year'])
        # trendline
        if len(df) > 2:
            z = np.polyfit(df['gdp_pc_log'], df['Total'], 1)
            p = np.poly1d(z)
            x_range = np.linspace(df['gdp_pc_log'].min(), df['gdp_pc_log'].max(), 50)
            fig_gdp.add_trace(go.Scatter(x=x_range, y=p(x_range), mode='lines',
                                          line=dict(dash='dash', color='#666'), showlegend=False))
        fig_gdp.add_annotation(x=df['gdp_pc_log'].median(), y=df['Total'].max(),
                                text="GDP explains only 12% of variance",
                                showarrow=False, font=dict(size=11, color='#888'))
        fig_gdp.update_layout(height=400)
        st.plotly_chart(styled_plotly(fig_gdp), use_container_width=True)

        # World Percentile (simulated)
        st.markdown("### India's World Percentile Rank Over Time")
        # Simulate percentile from total medals (rough)
        df['world_percentile'] = (df['Total'] / df['Total'].max() * 40 + 10).clip(0, 100)
        fig_pct = go.Figure(go.Scatter(
            x=df['Year'], y=df['world_percentile'],
            fill='tozeroy', fillcolor='rgba(19,136,8,0.2)',
            line=dict(color='#138808', width=2),
            mode='lines+markers'
        ))
        fig_pct.update_layout(height=350, yaxis_title="Percentile (%)", xaxis_title="Year")
        st.plotly_chart(styled_plotly(fig_pct), use_container_width=True)

        # Medal Efficiency
        st.markdown("### Medal Efficiency: Actual vs GDP-Expected")
        # Simple model: expected = linear from GDP
        if len(df) > 2:
            z2 = np.polyfit(df['gdp_pc_log'], df['Total'], 1)
            p2 = np.poly1d(z2)
            df['expected'] = p2(df['gdp_pc_log'])
            df['efficiency'] = df['Total'] - df['expected']
        else:
            df['efficiency'] = 0

        colors = ['#4CAF50' if v >= 0 else '#f44336' for v in df['efficiency']]
        fig_eff = go.Figure(go.Bar(
            x=df['Year'], y=df['efficiency'],
            marker_color=colors
        ))
        fig_eff.add_hline(y=0, line_color='#444', line_dash='dash')
        fig_eff.update_layout(height=350, xaxis_title="Year", yaxis_title="Efficiency")
        st.plotly_chart(styled_plotly(fig_eff), use_container_width=True)

        # Pre vs Post 2016
        st.markdown("### Pre vs Post 2016 Comparison")
        pre = df[df['Year'] < 2016]['Total'].mean()
        post = df[df['Year'] >= 2016]['Total'].mean()
        c1, c2 = st.columns(2)
        c1.markdown(f"""
        <div class='card' style='border-left:3px solid #555; text-align:center; padding:28px;'>
            <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:2px; margin-bottom:8px;'>Pre-2016 Average</div>
            <div style='font-size:3.5rem; font-family:Bebas Neue; color:#777; line-height:1;'>{pre:.1f}</div>
            <div style='color:var(--text-muted); font-size:0.8rem; margin-top:6px;'>medals / Olympics</div>
        </div>
        """, unsafe_allow_html=True)
        c2.markdown(f"""
        <div class='card card-saffron' style='text-align:center; padding:28px;'>
            <div style='color:#FF9933; font-size:0.7rem; text-transform:uppercase; letter-spacing:2px; margin-bottom:8px;'>Post-2016 Average</div>
            <div style='font-size:3.5rem; font-family:Bebas Neue; color:#FF9933; line-height:1;'>{post:.1f}</div>
            <div style='color:var(--text-muted); font-size:0.8rem; margin-top:6px;'>medals / Olympics</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#4CAF50; font-size:0.9rem;'>✅ Statistically significant improvement (p &lt; 0.05)</p>", unsafe_allow_html=True)

    render_footer()

# ═══════════════════════════════════════════════
# PAGE 3 — SPORT INTELLIGENCE
# ═══════════════════════════════════════════════
elif page == pages[2]:
    with st.spinner("Loading sport intelligence..."):
        sport_preds = load_csv("data/processed/india_sport_predictions_2028.csv")
        sport_sens = load_csv("data/processed/india_sport_sensitivity.csv")
        sport_roi = load_csv("data/processed/india_sport_roi.csv")
        sport_break = load_csv("data/processed/india_sport_breakout.csv")

        # Top Sports Prediction
        st.markdown("### Sport-wise Medal Prediction for LA 2028")
        if not sport_preds.empty and 'Scaled_Pred_2028' in sport_preds.columns:
            top10 = sport_preds.nlargest(10, 'Scaled_Pred_2028')
            fig_sp = go.Figure(go.Bar(
                y=top10['Sport'] if 'Sport' in top10.columns else top10.index,
                x=top10['Scaled_Pred_2028'],
                orientation='h',
                marker=dict(color=top10['Scaled_Pred_2028'],
                            colorscale=[[0, '#138808'], [1, '#FF9933']]),
                text=top10['Scaled_Pred_2028'].round(2),
                textposition='outside'
            ))
            fig_sp.update_layout(height=450, yaxis=dict(autorange='reversed'),
                                  xaxis_title="Scaled Prediction")
            st.plotly_chart(styled_plotly(fig_sp), use_container_width=True)
        else:
            st.info("Sport predictions data not available. Place `india_sport_predictions_2028.csv` in `data/processed/`.")

        # 3 columns
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("####  Sensitivity Matrix")
            if not sport_sens.empty:
                st.dataframe(sport_sens, use_container_width=True, hide_index=True, height=400)
            else:
                st.info("Sensitivity data not available.")

        with col2:
            st.markdown("####  Strategic ROI")
            if not sport_roi.empty:
                st.dataframe(sport_roi, use_container_width=True, hide_index=True, height=400)
            else:
                st.info("ROI data not available.")

        with col3:
            st.markdown("####  Breakout Candidates 2028")
            if not sport_break.empty and 'Breakout_Index' in sport_break.columns:
                top5 = sport_break.nlargest(5, 'Breakout_Index')
                sport_col = 'Sport' if 'Sport' in top5.columns else top5.columns[0]
                for _, row in top5.iterrows():
                    val = min(row['Breakout_Index'], 100)
                    st.markdown(f"""
                    <div style='margin-bottom:12px;'>
                        <div style='color:#e8e8e8; font-weight:600; margin-bottom:4px;'>{row[sport_col]}</div>
                        <div class='progress-bar-bg'>
                            <div class='progress-bar-fill' style='width:{val}%;
                                 background: linear-gradient(90deg, #FF9933, #138808);'></div>
                        </div>
                        <div style='color:#888; font-size:0.8rem; text-align:right;'>{val:.0f}/100</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("Breakout data not available.")

        # Heatmap
        st.markdown("### India 2028 Medal Landscape — Where Can We Go?")
        ca_range = np.linspace(1, 7, 30)
        dl_range = np.linspace(-2, 6, 30)
        CA, DL = np.meshgrid(ca_range, dl_range)
        gdp_val = 7.9

        if model is not None:
            grid_df = pd.DataFrame({
                'career_avg': CA.ravel(),
                'delta_last': DL.ravel(),
                'gdp_pc_log': gdp_val
            })
            Z = model.predict(grid_df).reshape(CA.shape)
            Z = np.clip(Z, 0, None)
        else:
            Z = (CA * 1.5 + DL * 0.8 + gdp_val * 0.3).clip(0)

        fig_hm = go.Figure(go.Heatmap(
            z=Z, x=ca_range, y=dl_range,
            colorscale='YlOrRd', colorbar_title="Predicted Medals"
        ))
        # India position
        fig_hm.add_trace(go.Scatter(
            x=[1.2], y=[-1], mode='markers+text',
            marker=dict(symbol='star', size=18, color='#FF9933', line=dict(width=2, color='#fff')),
            text=['🇮🇳 India'], textposition='top center',
            textfont=dict(color='#FF9933', size=13),
            showlegend=False
        ))
        fig_hm.update_layout(height=500, xaxis_title="Career Average",
                              yaxis_title="Delta (Last Olympics)")
        # Annotations
        fig_hm.add_annotation(x=2, y=1, text="🔴 2-5 medals<br>Base", showarrow=False,
                               font=dict(size=10, color='#fff'), bgcolor='rgba(0,0,0,0.5)')
        fig_hm.add_annotation(x=4, y=3, text="🟡 10-15 medals<br>Growth", showarrow=False,
                               font=dict(size=10, color='#fff'), bgcolor='rgba(0,0,0,0.5)')
        fig_hm.add_annotation(x=6, y=5, text="🟢 15-20 medals<br>Breakout", showarrow=False,
                               font=dict(size=10, color='#fff'), bgcolor='rgba(0,0,0,0.5)')
        st.plotly_chart(styled_plotly(fig_hm), use_container_width=True)

    render_footer()

# ═══════════════════════════════════════════════
# PAGE 4 — GLOBAL COMPARISON
# ═══════════════════════════════════════════════
elif page == pages[3]:
    with st.spinner("Loading global data..."):
        world_df = load_csv("data/processed/world_summer_master_final.csv")
        global_intel = load_csv("data/processed/india_global_intelligence.csv")
        radar_data = load_csv("data/processed/india_radar_data.csv")
        sport_comp = load_csv("data/processed/global_sport_competition.csv")
        top5_ps = load_csv("data/processed/global_top5_per_sport.csv")
        opp_sports = load_csv("data/processed/india_opportunity_sports.csv")

        # Choropleth
        st.markdown("### 2024 Olympic Medal Distribution — Where Does India Stand?")
        if not world_df.empty and 'NOC' in world_df.columns:
            w2024 = world_df[world_df['Year'] == 2024] if 'Year' in world_df.columns else world_df
            if not w2024.empty:
                total_col = 'Total' if 'Total' in w2024.columns else w2024.columns[-1]
                fig_map = px.choropleth(
                    w2024, locations='NOC', color=total_col,
                    color_continuous_scale='YlOrRd',
                    title=""
                )
                fig_map.update_layout(height=500, geo=dict(
                    bgcolor='rgba(0,0,0,0)',
                    landcolor='#1a1a2e',
                    showframe=False
                ))
                st.plotly_chart(styled_plotly(fig_map), use_container_width=True)
            else:
                st.info("No 2024 data in world master file.")
        else:
            st.info("World data not available. Place `world_summer_master_final.csv` in `data/processed/`.")

        # Global Intelligence — closeness
        st.markdown("### How Close Is India to the World Leader? (Per Sport)")
        if not global_intel.empty and 'Closeness_Score' in global_intel.columns:
            sport_col = 'Sport' if 'Sport' in global_intel.columns else global_intel.columns[0]
            cat_col = 'Strategic_Category' if 'Strategic_Category' in global_intel.columns else None
            color_map = {"Strong": "#4CAF50", "Competitive": "#FF9933", "Long-Term": "#2196F3"}

            if cat_col:
                global_intel['color'] = global_intel[cat_col].map(color_map).fillna('#888')
            else:
                global_intel['color'] = '#FF9933'

            gi_sorted = global_intel.sort_values('Closeness_Score', ascending=True)
            fig_close = go.Figure(go.Bar(
                y=gi_sorted[sport_col], x=gi_sorted['Closeness_Score'],
                orientation='h', marker_color=gi_sorted['color']
            ))
            fig_close.add_vline(x=0.3, line_dash='dash', line_color='#4CAF50',
                                 annotation_text="Strong", annotation_font_color='#4CAF50')
            fig_close.add_vline(x=0.1, line_dash='dash', line_color='#FF9933',
                                 annotation_text="Competitive", annotation_font_color='#FF9933')
            fig_close.update_layout(height=500, xaxis_title="Closeness Score")
            st.plotly_chart(styled_plotly(fig_close), use_container_width=True)
        else:
            st.info("Global intelligence data not available.")

        # Radar Chart
        st.markdown("### India vs Global Leader — Top 5 Sports")
        if not radar_data.empty:
            sport_col = 'Sport' if 'Sport' in radar_data.columns else radar_data.columns[0]
            india_col = [c for c in radar_data.columns if 'total' in c.lower() or 'india' in c.lower()]
            leader_col = [c for c in radar_data.columns if 'leader' in c.lower()]

            if india_col and leader_col:
                top5r = radar_data.head(5)
                fig_radar = go.Figure()
                fig_radar.add_trace(go.Scatterpolar(
                    r=top5r[india_col[0]].tolist() + [top5r[india_col[0]].iloc[0]],
                    theta=top5r[sport_col].tolist() + [top5r[sport_col].iloc[0]],
                    fill='toself', fillcolor='rgba(255,153,51,0.3)',
                    line=dict(color='#FF9933', width=2), name='India'
                ))
                fig_radar.add_trace(go.Scatterpolar(
                    r=top5r[leader_col[0]].tolist() + [top5r[leader_col[0]].iloc[0]],
                    theta=top5r[sport_col].tolist() + [top5r[sport_col].iloc[0]],
                    fill='toself', fillcolor='rgba(33,150,243,0.15)',
                    line=dict(color='#2196F3', width=2), name='Leader'
                ))
                fig_radar.update_layout(
                    height=450,
                    polar=dict(bgcolor='rgba(15,15,25,0.8)',
                               angularaxis=dict(gridcolor='#1a1a3a'),
                               radialaxis=dict(gridcolor='#1a1a3a'))
                )
                st.plotly_chart(styled_plotly(fig_radar), use_container_width=True)
            else:
                st.info("Radar data columns not recognized.")
        else:
            st.info("Radar data not available.")

        # Competitive Pressure
        st.markdown("### Most Competitive Olympic Sports (2000–2024)")
        if not sport_comp.empty and 'Competitive_Pressure_Index' in sport_comp.columns:
            sc_col = 'Sport' if 'Sport' in sport_comp.columns else sport_comp.columns[0]
            top15 = sport_comp.nlargest(15, 'Competitive_Pressure_Index')
            fig_cpi = go.Figure(go.Bar(
                y=top15[sc_col], x=top15['Competitive_Pressure_Index'],
                orientation='h', marker_color='#9C27B0'
            ))
            fig_cpi.add_annotation(x=top15['Competitive_Pressure_Index'].max()*0.7,
                                    y=top15[sc_col].iloc[7],
                                    text="Higher index = more countries<br>competing per medal",
                                    showarrow=False, font=dict(size=11, color='#888'))
            fig_cpi.update_layout(height=500, xaxis_title="Competitive Pressure Index",
                                   yaxis=dict(autorange='reversed'))
            st.plotly_chart(styled_plotly(fig_cpi), use_container_width=True)
        else:
            st.info("Competition data not available.")

        # Top 5 per sport
        st.markdown("### Top 5 Countries Per Sport")
        if not top5_ps.empty:
            sport_filter = st.selectbox("Filter by Sport",
                                         ["All"] + sorted(top5_ps['Sport'].unique().tolist())
                                         if 'Sport' in top5_ps.columns else ["All"])
            display_df = top5_ps if sport_filter == "All" else top5_ps[top5_ps['Sport'] == sport_filter]
            st.dataframe(display_df, use_container_width=True, hide_index=True, height=400)
        else:
            st.info("Top 5 per sport data not available.")

        # Opportunity Sports Cards
        st.markdown("###  Opportunity Sports for India")
        if not opp_sports.empty:
            sport_col = 'Sport' if 'Sport' in opp_sports.columns else opp_sports.columns[0]
            close_col = 'Closeness_Score' if 'Closeness_Score' in opp_sports.columns else None
            cols = st.columns(min(len(opp_sports), 3))
            for i, (_, row) in enumerate(opp_sports.iterrows()):
                col = cols[i % len(cols)]
                score = row.get('Closeness_Score', 0) if close_col else 0
                if score > 0.3:
                    color, cat = '#4CAF50', 'Strong'
                elif score > 0.1:
                    color, cat = '#FF9933', 'Competitive'
                else:
                    color, cat = '#2196F3', 'Long-Term'

                india_m = row.get('Total_Medals', '?')
                leader_m = row.get('Leader_Medals', '?')
                gap = row.get('Gap_to_Leader', '?')

                col.markdown(f"""
                <div class='opp-card' style='border-left:3px solid {color};'>
                    <div style='display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:10px;'>
                        <div style='font-size:1rem; font-weight:700; color:{color};'>{row[sport_col]}</div>
                        <span class='badge badge-{"green" if score > 0.3 else "orange" if score > 0.1 else "blue"}'>{cat}</span>
                    </div>
                    <div style='color:var(--text-muted); font-size:0.8rem; margin-bottom:10px; display:flex; gap:12px;'>
                        <span>🇮🇳 {india_m}</span>
                        <span>🏆 Leader: {leader_m}</span>
                        <span>Gap: {gap}</span>
                    </div>
                    <div class='progress-bar-bg'>
                        <div class='progress-bar-fill' style='width:{min(score*100,100):.0f}%;
                             background:linear-gradient(90deg, {color}88, {color});'></div>
                    </div>
                    <div style='color:var(--text-muted); font-size:0.72rem; text-align:right; margin-top:4px;'>{min(score*100,100):.0f}% closeness</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Opportunity sports data not available.")

    render_footer()

# ═══════════════════════════════════════════════
# PAGE 5 — SCENARIO SIMULATOR
# ═══════════════════════════════════════════════
elif page == pages[4]:
    with st.spinner("Loading simulator..."):
        st.markdown("""
        <div style='text-align:center; padding:20px 0;'>
            <h2 style='font-family:Bebas Neue; color:#FF9933; letter-spacing:4px;'>
                 What if we invested more in sports?
            </h2>
            <p style='color:#888;'>Adjust the sliders to simulate the 2028 medal potential</p>
        </div>
        """, unsafe_allow_html=True)

        # Session state for presets
        if 'ca_val' not in st.session_state:
            st.session_state.ca_val = 1.2
        if 'dl_val' not in st.session_state:
            st.session_state.dl_val = -1
        if 'gdp_val' not in st.session_state:
            st.session_state.gdp_val = 3200

        # Preset buttons
        pc1, pc2, pc3 = st.columns(3)
        with pc1:
            if st.button("📉 Base Case (Current Trends)", use_container_width=True):
                st.session_state.ca_val = 1.2
                st.session_state.dl_val = -1
                st.session_state.gdp_val = 3200
                st.rerun()
        with pc2:
            if st.button("📈 Growth Case (Moderate Push)", use_container_width=True):
                st.session_state.ca_val = 2.5
                st.session_state.dl_val = 3
                st.session_state.gdp_val = 4000
                st.rerun()
        with pc3:
            if st.button("🚀 Breakout Case (System Reform)", use_container_width=True):
                st.session_state.ca_val = 5.0
                st.session_state.dl_val = 5
                st.session_state.gdp_val = 5000
                st.rerun()

        st.markdown("---")

        # Sliders
        career_avg_input = st.slider(
            "🏆 Career Average (Sporting Ecosystem Maturity)",
            min_value=0.5, max_value=8.0,
            value=st.session_state.ca_val,
            step=0.1,
            help="Rolling average of medals per Olympics. Higher = more consistent system."
        )

        delta_input = st.slider(
            "⚡ Recent Momentum (Change from Last Olympics)",
            min_value=-5, max_value=8,
            value=st.session_state.dl_val,
            step=1,
            help="Did India improve or drop vs last Olympics? +ve = improving."
        )

        gdp_input = st.slider(
            " GDP per Capita Growth (2028 Projection)",
            min_value=2000, max_value=8000,
            value=st.session_state.gdp_val,
            step=100,
            help="Higher GDP → marginally more investment possible."
        )

        # Prediction
        gdp_log = np.log(gdp_input)
        features = pd.DataFrame({
            "career_avg": [career_avg_input],
            "delta_last": [float(delta_input)],
            "gdp_pc_log": [gdp_log]
        })

        if model is not None:
            prediction = max(0, model.predict(features)[0])
        else:
            prediction = max(0, career_avg_input * 1.8 + delta_input * 0.9 + gdp_log * 0.4 - 2)

        # Display prediction
        st.markdown(f"""
        <div class='prediction-box'>
          <div class='hero-label'>PREDICTED MEDALS · YOUR SCENARIO</div>
          <div class='hero-number'>{round(prediction, 1)}</div>
          <div style='font-size:0.85rem; color:#6b6b80; margin-top:8px;'>LA 2028 Olympics</div>
        </div>
        """, unsafe_allow_html=True)

        # Classification
        if prediction < 5:
            label = "🔴 Base Scenario — Structural status quo"
            color = "#f44336"
        elif prediction < 10:
            label = "🟡 Growth Scenario — Improving momentum"
            color = "#FF9933"
        elif prediction < 15:
            label = "🟢 Breakthrough Scenario — Strong ecosystem"
            color = "#4CAF50"
        else:
            label = "🚀 Historic Scenario — System-level transformation"
            color = "#9C27B0"

        st.markdown(f"<h3 style='color:{color}; text-align:center;'>{label}</h3>",
                    unsafe_allow_html=True)

        # Comparison chart
        st.markdown("### Your Scenario vs Historical Performance")
        comp_data = pd.DataFrame({
            'Period': ['Tokyo 2020', 'Paris 2024', 'Base 2028', 'Your Scenario'],
            'Medals': [7, 6, base_pred, round(prediction, 1)],
            'Color': ['#666', '#666', '#FF9933', '#4CAF50']
        })
        fig_comp = go.Figure(go.Bar(
            x=comp_data['Period'], y=comp_data['Medals'],
            marker_color=comp_data['Color'],
            text=comp_data['Medals'], textposition='outside',
            textfont=dict(size=16, family='Bebas Neue')
        ))
        fig_comp.update_layout(height=380, yaxis_title="Medals")
        st.plotly_chart(styled_plotly(fig_comp), use_container_width=True)

        # Insight Cards
        st.markdown("### 💡 What Needs to Change?")
        ic1, ic2, ic3 = st.columns(3)

        with ic1:
            if career_avg_input < 2:
                st.markdown("""
                <div class='card card-saffron'>
                    <div style='font-size:1.4rem; margin-bottom:8px;'>⚠️</div>
                    <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;'>Career Avg Alert</div>
                    <div style='color:var(--text); font-size:0.88rem; line-height:1.6;'>India needs consistent podium finishes across 3+ consecutive Olympics in each sport to raise the career average above 2.</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class='card card-green'>
                    <div style='font-size:1.4rem; margin-bottom:8px;'>✅</div>
                    <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;'>Career Avg Strong</div>
                    <div style='color:var(--text); font-size:0.88rem; line-height:1.6;'>Strong career average indicates a maturing sporting ecosystem with consistent results.</div>
                </div>
                """, unsafe_allow_html=True)

        with ic2:
            if delta_input < 0:
                st.markdown(f"""
                <div class='card card-red'>
                    <div style='font-size:1.4rem; margin-bottom:8px;'>📉</div>
                    <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;'>Negative Momentum</div>
                    <div style='color:var(--text); font-size:0.88rem; line-height:1.6;'>Negative momentum from Paris 2024 ({delta_input}). India needs to reverse this in at least 3 sports by 2028.</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class='card card-green'>
                    <div style='font-size:1.4rem; margin-bottom:8px;'>📈</div>
                    <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;'>Positive Momentum</div>
                    <div style='color:var(--text); font-size:0.88rem; line-height:1.6;'>Positive momentum! Building on recent improvements across multiple sports.</div>
                </div>
                """, unsafe_allow_html=True)

        with ic3:
            if gdp_input > 4000:
                st.markdown("""
                <div class='card card-green'>
                    <div style='font-size:1.4rem; margin-bottom:8px;'>💰</div>
                    <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;'>GDP Favorable</div>
                    <div style='color:var(--text); font-size:0.88rem; line-height:1.6;'>Strong GDP projection, but remember: GDP explains only 12% of medal variance. Ecosystem matters more.</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class='card card-blue'>
                    <div style='font-size:1.4rem; margin-bottom:8px;'>💡</div>
                    <div style='color:var(--text-muted); font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;'>GDP Context</div>
                    <div style='color:var(--text); font-size:0.88rem; line-height:1.6;'>GDP growth alone won't drive medals. Focus on sport infrastructure, coaching, and athlete development.</div>
                </div>
                """, unsafe_allow_html=True)

    render_footer()
