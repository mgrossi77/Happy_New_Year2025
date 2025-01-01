# Happy New Year 2025 App
import streamlit as st
from random import randint

# Display header
st.title("🎉 Happy New Year 2025 🎉")

# Loop to display symbols
for i in range(1, 1000):
    space = ' ' * randint(1, 100)
    if i % 10 == 0:
        st.text(space + 'Happy New Year 2025 🎉')
    elif i % 9 == 0:
        st.text(space + "🪅")
    elif i % 5 == 0:
        st.text(space + "🎈")
    elif i % 8 == 0:
        st.text(space + "🎈")
    elif i % 7 == 0:
        st.text(space + "🍁")
    elif i % 6 == 0:
        st.text(space + "❤️")
    else:
        st.text(space + "🔸")
