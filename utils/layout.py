#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 16:29
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   layout.py
# @Desc     :   

from streamlit import set_page_config, Page, navigation, session_state

from utils.login import authority_checker


def window_setter() -> None:
    """ Set the window configuration.
    :return: None
    """
    set_page_config(
        page_title="Private Agora",
        page_icon=":material/local_convenience_store:",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def subpages_setter() -> None:
    """ Set the subpages on the sidebar.
    :return: None
    """
    # Check the authentication status of the user
    if not session_state.get("authenticated", False):
        authority_checker()
        return
    else:
        pages: dict = {
            "page": [
                "subpages/home.py",
                "subpages/about.py",
            ],
            "title": [
                "Home",
                "About",
            ],
            "icon": [
                ":material/home:",
                ":material/info:",
            ],
        }

        structure: dict = {
            "Introduction": [
                Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
            ],
            "Core Functions": [

            ],
            "Information": [
                Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
            ],
        }
        pg = navigation(structure, position="sidebar", expanded=True)
        pg.run()
