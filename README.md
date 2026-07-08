# Nalybecks Hairstyles — Streamlit Website

An afrofuturistic-themed website for Nalybecks Hairstyles, covering:

- ⚡ Natural Hair Mastery (home page overview)
- 🔮 Afrofuturistic Hairstyles & Hair Art (gallery, filterable by category)
- 🎨 Custom Hair Art: Boards, Prints & NFTs (with commission request form)
- 💡 Smart Hair Accessories (product showcase + recommendation tool)
- 📅 Booking page with a request form

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## Structure

```
nalybecks_hairstyles/
├── app.py                          # Home page
├── theme.py                        # Shared CSS theme & color gradients
├── requirements.txt
└── pages/
    ├── 1_🔮_Hairstyles_Gallery.py
    ├── 2_🎨_Custom_Hair_Art.py
    ├── 3_💡_Smart_Accessories.py
    └── 4_📅_Booking.py
```

## Customize

- Replace placeholder contact info (phone, address, email, social handles) in
  `app.py` and `pages/4_📅_Booking.py`.
- Swap the emoji/gradient "swatches" in the gallery, hair art, and
  accessories pages with real photos using `st.image()` once you have
  photography assets — just add image files and reference them in place of
  the `<div class="swatch">` blocks.
- Hook the booking and commission forms up to email/CRM (e.g. via
  `smtplib`, Airtable API, or a form service) inside the `if submitted:`
  blocks.
- Add your NFT marketplace link in `pages/2_🎨_Custom_Hair_Art.py`.
