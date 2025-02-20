import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Set page config for a wider layout
st.set_page_config(layout="wide", page_title="Dr. Beardicus' Theorem", page_icon="🧔")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stMarkdown {
        font-size: 1.1rem;
    }
    .latex-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        color: #262730;
        border: 1px solid #e0e0e0;
    }
    /* Only apply dark color to elements with light backgrounds */
    .element-container:has(.latex-box) div[data-testid="stMarkdownContainer"] {
        color: #262730;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("🧔 Dr. Beardicus' Theorem: The Mathematics of Anime Avatars")
st.markdown("---")

# Introduction from the story
st.markdown("""
In the sprawling digital kingdom of the internet, where avatars reign supreme, 
Dr. Beardicus discovered an intriguing correlation between anime profile pictures 
and their users' facial hair characteristics.
""")

# Core Mathematical Definitions in LaTeX
st.markdown("### 📐 Core Mathematical Definitions")
st.markdown("""
<div class='latex-box'>
Let A ∈ [0,10] denote the cuteness level of an anime profile picture.

The beard prominence (B) is given by:

$B = \\frac{A^2}{10}$

The probability (P) of being a Medieval Fantasy Dwarf is:

$P = \\frac{1}{1 + e^{-(A - 8)}}$
</div>
""", unsafe_allow_html=True)

# Display the screenshots in a grid with explanations
st.markdown("### 🖼️ Example Cases of Medieval Fantasy Dwarfs")
col1, col2 = st.columns(2)

with col1:
    st.image("screenshots/1.png", caption="Example 1", use_container_width=True)
    st.latex(r"A = 5 \implies B = \frac{5^2}{10} = 2.5")
    st.image("screenshots/3.png", caption="Example 3", use_container_width=True)
    st.latex(r"A = 9 \implies B = \frac{81}{10} = 8.1")

with col2:
    st.image("screenshots/2.png", caption="Example 2", use_container_width=True)
    st.latex(r"A = 7 \implies B = \frac{49}{10} = 4.9")
    st.image("screenshots/theyhavebeards.jpg", caption="They Have Beards!", use_container_width=True)
    st.latex(r"A = 10 \implies B = \frac{100}{10} = 10")

st.markdown("---")

# Interactive Visualization Section
st.markdown("### 📊 Interactive Visualizations")

# Define the range for Cuteness Level (A)
A = np.arange(0, 10.1, 0.1)
B = (A**2) / 10
P = 1 / (1 + np.exp(-(A - 8)))

# Create tabs for different visualizations
tab1, tab2, tab3 = st.tabs(["Beard Prominence", "Medieval Fantasy Dwarf Probability", "Combined Analysis"])

with tab1:
    st.markdown("""
    #### Beard Prominence vs. Cuteness Level
    The relationship between cuteness level and beard prominence follows a quadratic curve:
    $B = \\frac{A^2}{10}$
    """)
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(A, B, label='Beard Prominence (B)', color='blue')
    ax1.set_xlabel('Cuteness Level (A)')
    ax1.set_ylabel('Beard Prominence (B)')
    ax1.grid(True)
    ax1.legend()
    st.pyplot(fig1)

with tab2:
    st.markdown("""
    #### Medieval Fantasy Dwarf Probability vs. Cuteness Level
    The probability of being a Medieval Fantasy Dwarf follows a sigmoid curve:
    $P = \\frac{1}{1 + e^{-(A - 8)}}$
    """)
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(A, P, label='Medieval Fantasy Dwarf Probability (P)', color='green')
    ax2.set_xlabel('Cuteness Level (A)')
    ax2.set_ylabel('Medieval Fantasy Dwarf Probability (P)')
    ax2.grid(True)
    ax2.legend()
    st.pyplot(fig2)

with tab3:
    st.markdown("""
    #### Combined Analysis
    Observe how both metrics evolve with increasing cuteness levels:
    """)
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    ax3.plot(A, B, label='Beard Prominence (B)', color='blue')
    ax3.set_xlabel('Cuteness Level (A)')
    ax3.set_ylabel('Beard Prominence (B)', color='blue')
    ax3.tick_params(axis='y', labelcolor='blue')

    ax4 = ax3.twinx()
    ax4.plot(A, P, label='Medieval Fantasy Dwarf Probability (P)', color='green')
    ax4.set_ylabel('Medieval Fantasy Dwarf Probability (P)', color='green')
    ax4.tick_params(axis='y', labelcolor='green')

    ax3.grid(True)
    ax3.legend(loc='upper left')
    ax4.legend(loc='upper right')
    st.pyplot(fig3)

# Key Findings Section
st.markdown("### 🔍 Key Findings")
st.markdown("""
<div class='latex-box'>
For specific cuteness levels:

1. **Moderate Cuteness** (A = 5):
   * Beard Prominence: $B = \\frac{5^2}{10} = 2.5$
   * Medieval Fantasy Dwarf Probability: $P \\approx 4.7\\%$

2. **High Cuteness** (A = 9):
   * Beard Prominence: $B = \\frac{9^2}{10} = 8.1$
   * Medieval Fantasy Dwarf Probability: $P \\approx 73.1\\%$

3. **Maximum Cuteness** (A = 10):
   * Beard Prominence: $B = \\frac{10^2}{10} = 10$
   * Medieval Fantasy Dwarf Probability: $P \\approx 88.1\\%$
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
*This visualization is based on Dr. Beardicus' groundbreaking research 
presented on X.com.*
""")
