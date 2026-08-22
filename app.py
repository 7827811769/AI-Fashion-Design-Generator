import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Fashion Design Generator",
    page_icon="👗",
    layout="centered"
)

st.title("👗 AI Fashion Design Generator")
st.write("Generate creative fashion design concepts using Google Gemini AI.")

try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("Gemini API key is not configured. Add GEMINI_API_KEY to Streamlit Secrets.")
    st.stop()

client = genai.Client(api_key=API_KEY)


def generate_fashion_design(gender, occasion, style, garment, color, fabric):
    prompt = f"""
You are an AI fashion designer.

Create a creative fashion design using:

Gender: {gender}
Occasion: {occasion}
Style: {style}
Garment: {garment}
Color: {color}
Fabric: {fabric}

Give the result with these sections:

DESIGN NAME
DESIGN CONCEPT
SILHOUETTE
FABRIC
COLOR
EMBELLISHMENT
ACCESSORIES
FOOTWEAR
STYLING
IMAGE PROMPT
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text


with st.form("fashion_form"):
    gender = st.selectbox("Gender", ["Women", "Men", "Unisex"])
    occasion = st.selectbox(
        "Occasion",
        ["Wedding", "Party", "Casual", "Formal", "Festival", "Evening Wear"]
    )
    style = st.selectbox(
        "Fashion Style",
        ["Modern Indian", "Traditional", "Modern", "Luxury", "Elegant"]
    )
    garment = st.selectbox(
        "Garment",
        ["Lehenga", "Saree", "Kurta", "Anarkali", "Dress", "Suit", "Gown"]
    )
    color = st.text_input("Color", value="Emerald Green")
    fabric = st.selectbox(
        "Fabric",
        ["Silk", "Cotton", "Velvet", "Chiffon", "Organza"]
    )

    submitted = st.form_submit_button("✨ Generate Fashion Design")

if submitted:
    with st.spinner("Generating your fashion design..."):
        try:
            design_output = generate_fashion_design(
                gender, occasion, style, garment, color, fabric
            )
            st.subheader("✨ Generated Fashion Design")
            st.markdown(design_output)
        except Exception as e:
            st.error(
                "The AI request could not be completed right now. "
                "Please try again in a moment."
            )
            st.caption(f"Technical details: {e}")
