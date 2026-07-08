import streamlit as st
from theme import load_css, GRADIENTS

st.set_page_config(page_title="Smart Accessories | Nalybecks", page_icon="💡", layout="wide")
load_css()

st.markdown('<div class="page-title">💡 Smart Hair Accessories</div>', unsafe_allow_html=True)
st.markdown("Style meets innovation — accessories designed for natural hair health and futuristic flair.")
st.write("")

products = [
    ("🔆", "LED Hair Cuffs", "$28", "Rechargeable light-up hair cuffs for locs, braids & twists — multiple color modes."),
    ("🌡️", "Scalp Health Sensor Clip", "$65", "Discreet clip that tracks scalp moisture & temperature, syncing to a companion app."),
    ("🧲", "Magnetic Loc Jewelry Set", "$34", "No-damage magnetic attachment jewelry for locs and braids."),
    ("💧", "Smart Mist Applicator", "$42", "Fine-mist sprayer with app-guided moisture reminders for natural hair care."),
    ("🎧", "Bone-Conduction Headwrap", "$89", "Satin-lined headwrap with built-in bone-conduction audio — protects hair while you listen."),
    ("⚙️", "UV-Reactive Hair Cuffs", "$22", "Color-shifting cuffs that react to sunlight for an ever-changing look."),
]

cols = st.columns(3)
for i, (icon, name, price, desc) in enumerate(products):
    with cols[i % 3]:
        grad = GRADIENTS[i % len(GRADIENTS)]
        st.markdown(f"""
        <div class="glow-card">
            <div class="swatch" style="background:{grad};">{icon}</div>
            <h3>{name}</h3>
            <p class="price-tag">{price}</p>
            <p style="color:#d8c9ff; font-size:0.88rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.markdown("---")
st.markdown("### 🧪 Care Companion")
st.markdown("Use the quick tool below to get a smart-accessory recommendation based on your hair type and goals.")

hair_type = st.selectbox("Your natural hair type", ["Coily (4A-4C)", "Curly (3A-3C)", "Wavy (2A-2C)", "Locs", "Braided/Protective style"])
goal = st.radio("Primary goal", ["Moisture tracking", "Style enhancement (light/jewelry)", "Protection while active/sleeping"], horizontal=True)

if st.button("Get Recommendation"):
    if goal == "Moisture tracking":
        rec = "Scalp Health Sensor Clip 🌡️ + Smart Mist Applicator 💧"
    elif goal == "Style enhancement (light/jewelry)":
        rec = "LED Hair Cuffs 🔆 + UV-Reactive Hair Cuffs ⚙️"
    else:
        rec = "Bone-Conduction Headwrap 🎧 + Magnetic Loc Jewelry Set 🧲"
    st.success(f"For your {hair_type} hair with a focus on **{goal.lower()}**, we recommend: **{rec}**")
