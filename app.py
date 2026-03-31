import streamlit as st
from chemistry import chemistry_lab

st.set_page_config(
    page_title="AI Chemistry Virtual Lab",
    page_icon="🧪",
    layout="wide"
)

# -------- WATERMARK --------
st.markdown("""
<style>
.watermark {
    position: fixed;
    bottom: 10px;
    right: 15px;
    opacity: 0.35;
    font-size: 0.8rem;
    color: #9ca3af;
    text-align: right;
}
</style>

<div class="watermark">
    Atrijo Das (35)<br>
    Sohan Pramanik (34)<br>
    Sharanya Mallick (30)<br>
    Swagata Mukherjee (40)
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Navigate", ["Home", "Experiments"])

if page == "Home":
    st.title("🧪 AI Chemistry Virtual Lab")
    st.write("Interactive Chemistry Experiments with Graphs & Viva")

elif page == "Experiments":
    chemistry_lab()
