#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 16:29
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :   

from streamlit import title, divider, expander, caption, empty

title("PRIVATE AGORA")
divider()

empty_messages: empty = empty()
empty_messages.info("Welcome to Private Agora!")

with expander("Application Introduction", expanded=True):
    caption("Private Agora is a demo platform for trading private data.")
