#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 14:44
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :   

from streamlit import sidebar, empty

from utils.layout import (window_setter, subpages_setter, sidebar_hider,
                          session_state)
from utils.login import authority_checker


def main() -> None:
    """ streamlit run main.py """
    # Set the window configuration
    window_setter()

    # Set the subpages on the sidebar
    if not session_state.get("authenticated", False):
        # If the user is not authenticated, show the login page
        authority_checker()
        # Hide the sidebar, because the sidebar setting is global and will affect all pages, so hide it manually
        sidebar_hider()
    else:
        subpages_setter()


if __name__ == "__main__":
    main()
