#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/20 22:00
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   account.py
# @Desc     :   

from streamlit import (sidebar, subheader, divider, empty, text_input, button,
                       caption, spinner, session_state, rerun)

empty_messages: empty = empty()

with sidebar:
    subheader("Account Settings")
    pass
