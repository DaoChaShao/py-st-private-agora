#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 16:40
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   about.py
# @Desc     :   

from streamlit import title, divider, expander, caption, empty

title("About")
divider()

empty_messages: empty = empty()
empty_messages.info("This page provides information about the Private Agora application.")

with expander("Application Introduction", expanded=True):
    caption("Private Agora is a demo platform for trading private data.")
    caption("This application is designed to demonstrate the basic functionalities of a private data trading platform.")
    caption("It is not intended for real-world use and does not handle any sensitive or personal data.")
    caption("The application is built using Streamlit, a powerful framework for creating web applications in Python.")
