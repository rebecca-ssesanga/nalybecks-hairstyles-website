import streamlit as st
from theme import load_css, GRADIENTS

st.set_page_config(page_title="Custom Hair Art | Nalybecks", page_icon="🎨", layout="wide")
load_css()

st.markdown('<div class="page-title">🎨 Custom Hair Art: Boards, Prints & NFTs</div>', unsafe_allow_html=True)
st.markdown("Wearable culture, framed art, and digital collectibles — all born from natural hair as a canvas.")
st.write("")

tab1, tab2, tab3 = st.tabs(["🧵 Hair Boards", "🖼️ Prints", "🪙 NFTs"])

with tab1:
    st.markdown("#### Hand-crafted Hair Boards")
    st.markdown("Sculptural boards made from real and synthetic hair fiber, arranged into afrofuturistic patterns and mounted for display.")
    c1, c2, c3 = st.columns(3)
    boards = [
        ("🌀", "Spiral Galaxy Board", "$180"),
        ("🪐", "Orbit Pattern Board", "$220"),
        ("⚡", "Circuit Weave Board", "$250"),
    ]
    for col, (icon, name, price) in zip([c1, c2, c3], boards):
        with col:
            grad = GRADIENTS[hash(name) % len(GRADIENTS)]
            st.markdown(f"""
            <div class="glow-card">
                <div class="swatch" style="background:{grad};">{icon}</div>
                <h3>{name}</h3>
                <p class="price-tag">{price}</p>
                <p style="color:#d8c9ff; font-size:0.88rem;">Custom sizing & color palette available on commission.</p>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("#### Fine Art Prints")
    st.markdown("Photographic and illustrated prints celebrating natural hair as futuristic art — available in multiple sizes and finishes.")
    c1, c2, c3 = st.columns(3)
    prints = [
        ("🌠", "Meteor Curls Print", "$45"),
        ("🔥", "Phoenix Updo Print", "$45"),
        ("💎", "Crystal Crown Print", "$55"),
    ]
    for col, (icon, name, price) in zip([c1, c2, c3], prints):
        with col:
            grad = GRADIENTS[hash(name) % len(GRADIENTS)]
            st.markdown(f"""
            <div class="glow-card">
                <div class="swatch" style="background:{grad};">{icon}</div>
                <h3>{name}</h3>
                <p class="price-tag">{price}</p>
                <p style="color:#d8c9ff; font-size:0.88rem;">Archival matte paper. Framing available.</p>
            </div>
            """, unsafe_allow_html=True)

with tab3:
    st.markdown("#### Hair Art NFTs")
    st.markdown("Limited-edition digital collectibles capturing original hair art pieces, minted as NFTs for collectors.")
    c1, c2, c3 = st.columns(3)
    nfts = [
        ("🪙", "Genesis Coil #001", "0.08 ETH", "Sold Out"),
        ("🪙", "Nebula Locs #014", "0.05 ETH", "Available"),
        ("🪙", "Circuit Braids #027", "0.06 ETH", "Available"),
    ]
    for col, (icon, name, price, status) in zip([c1, c2, c3], nfts):
        with col:
            grad = GRADIENTS[hash(name) % len(GRADIENTS)]
            st.markdown(f"""
            <div class="glow-card">
                <div class="swatch" style="background:{grad};">{icon}</div>
                <h3>{name}</h3>
                <p class="price-tag">{price}</p>
                <span class="badge">{status}</span>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.info("🔗 Connect your wallet details / marketplace link here once your NFT collection is live (e.g. OpenSea, Foundation).")

st.write("")
st.markdown("---")
st.markdown("### ✨ Commission a Custom Piece")
with st.form("commission_form"):
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Your name")
        email = st.text_input("Email")
    with c2:
        art_type = st.selectbox("Art type", ["Hair Board", "Print", "NFT", "Not sure yet"])
        budget = st.select_slider("Budget range", options=["$50-100", "$100-250", "$250-500", "$500+"])
    details = st.text_area("Tell us about your vision")
    submitted = st.form_submit_button("Submit Commission Request")
    if submitted:
        if name and email:
            st.success(f"✨ Thank you, {name}! Your commission request has been received. We'll email you at {email} soon.")
        else:
            st.warning("Please fill in your name and email.")
