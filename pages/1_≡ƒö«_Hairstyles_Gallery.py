import streamlit as st
from theme import load_css, GRADIENTS

st.set_page_config(page_title="Hairstyles Gallery | Nalybecks", page_icon="🔮", layout="wide")
load_css()

st.markdown('<div class="page-title">🔮 Afrofuturistic Hairstyles & Hair Art</div>', unsafe_allow_html=True)
st.markdown("Explore natural-hair mastery reimagined through a futuristic, cosmic lens.")
st.write("")

styles = [
    ("🌀", "Cosmic Coils", "Natural", "Defined natural coils sculpted with metallic accents for an out-of-this-world finish."),
    ("⚡", "Circuitry Braids", "Braids", "Geometric braid patterns inspired by circuit boards — precision meets tradition."),
    ("🌌", "Nebula Locs", "Locs", "Freeform or interlocked locs styled with galaxy-inspired color melts."),
    ("💎", "Crystal Crown Twist", "Twists", "Two-strand twists finished with crystal and metal hair jewelry."),
    ("🛸", "Starship Fade", "Cuts", "Natural texture top paired with a sharp, sculpted fade design."),
    ("🔥", "Phoenix Updo", "Updo", "Sculptural updo with sweeping shapes reminiscent of flight and flame."),
    ("🌠", "Meteor Shower Curls", "Curls", "Natural curl definition accented with shimmering strand highlights."),
    ("🪐", "Orbit Bantu Knots", "Protective", "Bantu knot formations arranged in orbital, symmetrical patterns."),
]

categories = ["All"] + sorted(set(s[2] for s in styles))
choice = st.selectbox("Filter by category", categories)

filtered = [s for s in styles if choice == "All" or s[2] == choice]

cols = st.columns(4)
for i, (icon, name, cat, desc) in enumerate(filtered):
    with cols[i % 4]:
        grad = GRADIENTS[i % len(GRADIENTS)]
        st.markdown(f"""
        <div class="glow-card">
            <div class="swatch" style="background:{grad};">{icon}</div>
            <span class="badge">{cat}</span>
            <h3 style="margin-top:0.3rem;">{name}</h3>
            <p style="color:#d8c9ff; font-size:0.9rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.markdown("---")
st.markdown("### 📸 Have a look you love?")
st.markdown("Bring inspiration photos to your consultation, or head to **Booking** to reserve your session and let's design something original together.")
