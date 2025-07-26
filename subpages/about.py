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
      - Budget-based **data purchasing simulation** using optimisation algorithms.
      - **Flat and structured data viewing**, allowing for easier exploration.
      - **Built-in database** operations to manage the lifecycle of synthetic data.
      - User-friendly **interface powered by Streamlit**, with live interaction and feedback.
    """)
    caption(
        "🛠️ Note: All data shown in the app is synthetically generated. "
        "It does not represent real users and is intended for safe exploration and simulation only."
    )
