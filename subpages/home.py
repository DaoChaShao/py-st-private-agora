#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 16:29
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :   

from streamlit import title, expander, caption, empty

title("PRIVATE AGORA")

empty_messages: empty = empty()
empty_messages.info("Welcome to Private Agora!")

with expander("Application Introduction", expanded=True):
    caption(
        "Welcome to Data Trading Simulator — Private Agora, "
        "a powerful and interactive platform designed to simulate the lifecycle of data "
        "— from generation and visualisation to trading and database management."
    )
    caption("This tool enables you to:")
    caption(
        "- 🧪 **Generate synthetic data** for various application domains "
        "like social media, short video, mobile payment, health & fitness, and maps & navigation."
    )
    caption("- 📊 **Visualize and explore data** dynamically based on selected quantity, duration, and category.")
    caption(
        "- 💾 **Manage your database** by creating, checking, inserting, displaying, "
        "and deleting synthetic user data using SQLite."
    )
    caption(
        "- 💸 **Simulate data trading** by setting a budget and selecting optimal datasets within your price range "
        "using a knapsack-style algorithm."
    )
    caption("- 📂 **Examine flattened data** from nested JSON structures for further analysis.")
    caption(
        "Whether you’re a student, researcher, or data enthusiast, "
        "this simulator helps you understand how personal data might be categorised, stored, "
        "and valued in a mock trading environment."
    )
