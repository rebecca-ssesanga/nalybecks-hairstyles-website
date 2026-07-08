import streamlit as st

st.set_page_config(
    page_title="Nalybecks Hairstyles | Natural Hair Mastery",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- GLOBAL AFROFUTURISTIC THEME ----------
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

    h1, h2, h3, .hero-title {
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 1px;
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ffd76e, #ff5cae, #7f5cff, #29e0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 300% 300%;
        animation: shimmer 6s ease infinite;
        margin-bottom: 0;
    }

    @keyframes shimmer {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .hero-sub {
        font-size: 1.25rem;
        color: #d8c9ff;
        font-weight: 300;
        margin-top: 0.2rem;
    }

    .glow-card {
        background: linear-gradient(145deg, rgba(127,92,255,0.12), rgba(255,92,174,0.08));
        border: 1px solid rgba(255,215,110,0.35);
        border-radius: 18px;
        padding: 1.4rem;
        box-shadow: 0 0 25px rgba(127,92,255,0.25);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        height: 100%;
    }

    .glow-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 0 40px rgba(255,92,174,0.45);
    }

    .glow-card h3 {
        color: #ffd76e;
        margin-top: 0;
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

    .cta-btn {
        background: linear-gradient(90deg, #7f5cff, #ff5cae);
        color: white !important;
        padding: 0.7rem 1.6rem;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 0 20px rgba(255,92,174,0.5);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #150429, #05000d);
        border-right: 1px solid rgba(255,215,110,0.2);
    }

    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

load_css()

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("### 🔮 NALYBECKS")
    st.caption("Natural Hair Mastery • Afrofuturism")
    st.markdown("---")
    st.markdown("📍 Studio Location: *Set your address here*")
    st.markdown("📞 Booking: *Set your phone here*")
    st.markdown("📧 hello@nalybecks.com")
    st.markdown("---")
    st.markdown("Use the **Pages** menu above ⬆️ to explore Hairstyles, Hair Art, Smart Accessories & Booking.")

# ---------- HERO ----------
st.markdown('<div class="hero-title">NALYBECKS HAIRSTYLES</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">⚡ Natural Hair Mastery — Where Ancestral Roots Meet Future Vision 🔮</div>', unsafe_allow_html=True)
st.write("")
st.write("")

col1, col2 = st.columns([1.3, 1])
with col1:
    st.markdown("""
    Nalybecks Hairstyles blends deep expertise in **natural hair care** with bold
    **afrofuturistic artistry**. From protective styles rooted in tradition to
    sculptural, sci-fi-inspired hair art, custom digital collectibles, and smart
    accessories — we craft looks that carry your story into the future.
    """)
    st.markdown('<a class="cta-btn" href="#book-a-session">✨ Book a Session</a>', unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="glow-card">
    <span class="badge">STUDIO STATUS</span>
    <h3>Now Booking</h3>
    <p>New client consultations available this week for natural hair transformations
    and custom hair art commissions.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("## 🌌 What We Do")

c1, c2, c3, c4 = st.columns(4)
services = [
    ("⚡", "Natural Hair Mastery", "Locs, twists, braids, coils & natural cuts — healthy hair rooted in expert technique."),
    ("🔮", "Afrofuturistic Styling", "Bold, sculptural hairstyles and hair art inspired by cosmic & futuristic aesthetics."),
    ("🎨", "Custom Hair Art", "Hand-crafted hair boards, photographic prints, and limited-edition hair art NFTs."),
    ("💡", "Smart Accessories", "Curated smart hair tech & accessories designed for style, care, and innovation."),
]
for col, (icon, title, desc) in zip([c1, c2, c3, c4], services):
    with col:
        st.markdown(f"""
        <div class="glow-card">
        <div style="font-size:2rem;">{icon}</div>
        <h3>{title}</h3>
        <p style="color:#d8c9ff; font-size:0.92rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.markdown("---")
st.markdown("## 💬 Why Nalybecks")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="glow-card">
    <h3>🌿 Rooted Expertise</h3>
    <p style="color:#d8c9ff;">Years mastering natural hair textures, healthy scalp practices, and protective styling.</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="glow-card">
    <h3>🚀 Forward Vision</h3>
    <p style="color:#d8c9ff;">Afrofuturism as a creative language — merging ancestral pride with tomorrow's aesthetics.</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="glow-card">
    <h3>🖤 One-of-One Art</h3>
    <p style="color:#d8c9ff;">Every hair board, print, and NFT is an original piece — wearable and collectible culture.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("---")
st.markdown('<h3 id="book-a-session">📅 Ready to Begin Your Transformation?</h3>', unsafe_allow_html=True)
st.markdown("Head to the **Booking** page in the sidebar to reserve your session, or explore the **Gallery**, **Hair Art**, and **Smart Accessories** pages first.")
