# Happy New Year 2025 App
import streamlit as st
import time
from random import randint

# Set up the title
st.title("🎉 Happy New Year 2025 🎉")

# Create a placeholder for dynamic updates
placeholder = st.empty()

# Dynamic content
for i in range(1, 1000):
    space = ' ' * randint(1, 100)
    if i % 10 == 0:
        text = space + 'Happy New Year 2025 🎉'
    elif i % 9 == 0:
        text = space + "🪅"
    elif i % 5 == 0:
        text = space + "🎈"
    elif i % 8 == 0:
        text = space + "🎈"
    elif i % 7 == 0:
        text = space + "🍁"
    elif i % 6 == 0:
        text = space + "❤️"
    else:
        text = space + "🔸"

    # Update the placeholder
    placeholder.text(text)

    # Pause for a moment to simulate animation
    time.sleep(0.2)

