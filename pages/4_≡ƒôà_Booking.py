import streamlit as st
from datetime import date, timedelta
from theme import load_css

st.set_page_config(page_title="Booking | Nalybecks", page_icon="📅", layout="wide")
load_css()

st.markdown('<div class="page-title">📅 Book a Session</div>', unsafe_allow_html=True)
st.markdown("Reserve your spot for a natural hair styling session, hair art consultation, or smart accessory fitting.")
st.write("")

col1, col2 = st.columns([1.2, 1])

with col1:
    with st.form("booking_form"):
        st.markdown("#### Your Details")
        name = st.text_input("Full name")
        c1, c2 = st.columns(2)
        with c1:
            email = st.text_input("Email")
        with c2:
            phone = st.text_input("Phone")

        st.markdown("#### Session Details")
        service = st.selectbox(
            "Service",
            [
                "Natural Hair Styling (Locs/Braids/Twists/Coils)",
                "Afrofuturistic Style Design",
                "Custom Hair Art Consultation (Board/Print/NFT)",
                "Smart Accessory Fitting",
                "Full Experience (Style + Art)",
            ],
        )
        min_date = date.today() + timedelta(days=1)
        preferred_date = st.date_input("Preferred date", min_value=min_date)
        preferred_time = st.selectbox("Preferred time", ["Morning (9am-12pm)", "Afternoon (12pm-4pm)", "Evening (4pm-7pm)"])
        notes = st.text_area("Anything we should know? (hair type, inspiration, allergies, etc.)")

        submitted = st.form_submit_button("✨ Request Booking")
        if submitted:
            if name and (email or phone):
                st.success(
                    f"Thank you, {name}! Your request for **{service}** on **{preferred_date.strftime('%B %d, %Y')}** "
                    f"({preferred_time}) has been received. We'll confirm shortly via your provided contact info."
                )
                st.balloons()
            else:
                st.warning("Please provide your name and at least one contact method (email or phone).")

with col2:
    st.markdown("""
    <div class="glow-card">
    <h3>🕐 Studio Hours</h3>
    <p style="color:#d8c9ff;">
    Tue – Fri: 9am – 7pm<br>
    Sat: 8am – 5pm<br>
    Sun – Mon: Closed
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glow-card">
    <h3>📍 Find Us</h3>
    <p style="color:#d8c9ff;">Studio address — set your location here.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glow-card">
    <h3>💌 Prefer to reach out directly?</h3>
    <p style="color:#d8c9ff;">
    📧 hello@nalybecks.com<br>
    📞 Set your phone number here<br>
    📱 @nalybeckshairstyles
    </p>
    </div>
    """, unsafe_allow_html=True)
