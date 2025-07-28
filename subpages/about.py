#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 16:40
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   about.py
# @Desc     :   

from streamlit import title, expander, caption, empty

title("About")

empty_messages: empty = empty()
empty_messages.info("This page provides information about the Private Agora application.")

with expander("Application About", expanded=True):
    caption("""
    - 📁 Data Categories:
      - **Social Media**: Engagement metrics such as likes, comments, shares, and watch duration.
      - **Short Video**: Includes video types, watch durations, and interaction history.
      - **Mobile Payment**: Captures device info, payment methods, transaction volumes and frequency.
      - **Health & Fitness**: Logs workouts, steps, calories burned, and health stats.
      - **Maps & Navigation**: Tracks travel habits, distances, and commuting data.
    """)
    caption("""
    - 🧩 Key Features:
      - Budget-based **data trading simulation** using knapsack optimisation.
      - **Structured and flattened data views**, ideal for inspection and downstream processing.
      - Built-in **database operations** for managing synthetic data lifecycle.
      - Seamless **integration with LLMs (OpenAI / DeepSeek)** for multilingual data interpretation and summarisation.
      - Streamlit-powered **interactive UI** for real-time exploration and feedback.
    """)
    caption(
        "🛠️ Note: All data shown in the app is synthetically generated. "
        "It does not represent real users and is intended for safe exploration and simulation only."
    )
