import streamlit as st

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at 20% 20%, #1b0836 0%, #0a0016 45%, #05000d 100%);
        color: #f2e9ff;
    }

    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 1px;
        color: #ffd76e;
    }

    .page-title {
        font-size: 2.6rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ffd76e, #ff5cae, #7f5cff, #29e0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 300% 300%;
        animation: shimmer 6s ease infinite;
        font-family: 'Orbitron', sans-serif;
    }

    @keyframes shimmer {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .glow-card {
        background: linear-gradient(145deg, rgba(127,92,255,0.12), rgba(255,92,174,0.08));
        border: 1px solid rgba(255,215,110,0.35);
        border-radius: 18px;
        padding: 1.4rem;
        box-shadow: 0 0 25px rgba(127,92,255,0.25);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        height: 100%;
        margin-bottom: 1rem;
    }

    .glow-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 0 40px rgba(255,92,174,0.45);
    }

    .badge {
        display: inline-block;
        background: rgba(41,224,255,0.15);
        color: #29e0ff;
        border: 1px solid #29e0ff;
        border-radius: 999px;
        padding: 0.25rem 0.9rem;
        font-size: 0.8rem;
        margin-bottom: 0.6rem;
    }

    .price-tag {
        color: #ffd76e;
        font-weight: 700;
        font-size: 1.1rem;
    }

    .swatch {
        border-radius: 16px;
        height: 160px;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.6rem;
        margin-bottom: 0.7rem;
        box-shadow: 0 0 20px rgba(0,0,0,0.4) inset;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #150429, #05000d);
        border-right: 1px solid rgba(255,215,110,0.2);
    }

    footer {visibility: hidden;}

    .stButton>button {
        background: linear-gradient(90deg, #7f5cff, #ff5cae);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.6rem 1.6rem;
        font-weight: 600;
        box-shadow: 0 0 20px rgba(255,92,174,0.4);
    }
    </style>
    """, unsafe_allow_html=True)


GRADIENTS = [
    "linear-gradient(135deg, #7f5cff, #29e0ff)",
    "linear-gradient(135deg, #ff5cae, #ffd76e)",
    "linear-gradient(135deg, #29e0ff, #05ffa1)",
    "linear-gradient(135deg, #ffd76e, #ff5cae)",
    "linear-gradient(135deg, #7f5cff, #ff5cae)",
    "linear-gradient(135deg, #05ffa1, #7f5cff)",
]
