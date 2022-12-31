import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We believe powdery mildew leaves show clear marks/signs; "
        f"such as the leaves are light roughly-circular, powders-looking patches on young, susceptible leaves (light green expanding leaves) that can differentiate, from healthy leaves. \n\n"
        f"* An Image Montage, shows that typically a powdery mildew leaves have fine white powdery marks across. "
        f"The Average Image, Variability Image, and Difference between Averages studies did not "
        f"reveal any clear patterns that would allow us to distinguish one from the other."

    )