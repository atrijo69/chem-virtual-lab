import streamlit as st
import numpy as np
from utils import plot_graph

def chemistry_lab():
    st.header("🧪 Chemistry Experiments")

    exp = st.selectbox("Choose Experiment", [
        "Acid-Base Titration",
        "pH Metric Titration",
        "Viscosity",
        "Surface Tension"
    ])

    # -------- ACID BASE --------
    if exp == "Acid-Base Titration":
        st.subheader("Acid-Base Titration")
        st.image("assets/titration.png", width=350)

        v1 = st.number_input("Volume of Acid (mL)", 1.0, 100.0, 10.0)
        s1 = st.number_input("Strength of Acid (N)", 0.1, 5.0, 1.0)
        v2 = st.number_input("Volume of Base (mL)", 1.0, 100.0, 10.0)

        if st.button("Calculate Base Strength"):
            s2 = (v1 * s1) / v2
            st.success(f"Base Strength = {s2:.2f} N")

        vol = np.linspace(0, 100, 50)
        curve = (vol / 40) * 7
        plot_graph(vol, curve, "Volume", "Neutralization", "Titration Curve")

        st.subheader("🎓 Viva Questions")
        with st.expander("What is titration?"):
            st.write("Method to determine concentration using standard solution.")
        with st.expander("What is equivalence point?"):
            st.write("Moles of acid = moles of base.")
        with st.expander("Why indicator is used?"):
            st.write("To detect endpoint by color change.")

    # -------- PH --------
    elif exp == "pH Metric Titration":
        st.subheader("pH Metric Titration")
        st.image("assets/ph_meter.png", width=350)

        volume = np.linspace(0, 100, 50)
        pH = 3 + (11 - 3) / (1 + np.exp(-(volume - 40)/5))
        plot_graph(volume, pH, "Volume", "pH", "pH Curve")

        st.subheader("🎓 Viva Questions")
        with st.expander("What is pH?"):
            st.write("Measure of acidity/basicity.")
        with st.expander("What is pH meter?"):
            st.write("Device to measure pH.")
        with st.expander("What happens at equivalence?"):
            st.write("Sharp pH change occurs.")

    # -------- VISCOSITY --------
    elif exp == "Viscosity":
        st.subheader("Viscosity")
        st.image("assets/viscometer.png", width=350)

        t1 = st.number_input("Liquid Time", 1.0, 200.0, 50.0)
        t2 = st.number_input("Water Time", 1.0, 200.0, 40.0)

        if st.button("Calculate Viscosity"):
            st.success(f"Ratio = {t1/t2:.2f}")

        plot_graph([1,2], [t1,t2], "Sample", "Time", "Comparison")

        st.subheader("🎓 Viva Questions")
        with st.expander("What is viscosity?"):
            st.write("Resistance to flow.")
        with st.expander("Instrument used?"):
            st.write("Ostwald viscometer.")
        with st.expander("Factors affecting viscosity?"):
            st.write("Temperature and nature of liquid.")

    # -------- SURFACE --------
    elif exp == "Surface Tension":
        st.subheader("Surface Tension")
        st.image("assets/stalagmometer.png", width=350)

        n1 = st.number_input("Liquid Drops", 1, 200, 50)
        n2 = st.number_input("Water Drops", 1, 200, 60)

        if st.button("Calculate Surface Tension"):
            st.success(f"Ratio = {n2/n1:.2f}")

        plot_graph([1,2], [n1,n2], "Sample", "Drops", "Comparison")

        st.subheader("🎓 Viva Questions")
        with st.expander("What is surface tension?"):
            st.write("Force acting on liquid surface.")
        with st.expander("Instrument used?"):
            st.write("Stalagmometer.")
        with st.expander("What affects it?"):
            st.write("Temperature and impurities.")
