import streamlit as st

from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=230)

with col2:
    st.title("Herbarium", anchor=False)
    st.write(
        "Welcome to our Herbarium Knowledge Base—your digital gateway to the fascinating world of plant science! This Python-powered platform is designed to catalog, organize, and share detailed information about plant specimens."
    )
    if st.button("✉️ Contribute"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Features:", anchor=False)
st.write(
    """
🌿 Comprehensive Plant Records: Access detailed profiles for plant specimens, including taxonomy, physical descriptions, habitats, and ecological significance.

📚 Learn & Share: Discover fascinating details about native, medicinal, or endangered plants, and contribute to the knowledge base by adding your findings.

💻 Python-Powered Precision: Built using Python, this platform leverages robust data management and machine learning capabilities for seamless and accurate information delivery.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Why use our Knowledge Base?", anchor=False)
st.write(
    """
-Easy-to-navigate design for all user levels.
-Continuously updated with the latest botanical research.
-Open-source and community-driven for transparency and collaboration.
    """
)
