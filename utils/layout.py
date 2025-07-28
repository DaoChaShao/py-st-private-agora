#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 16:29
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   layout.py
# @Desc     :   

from streamlit import (set_page_config, Page, navigation,
                       session_state, markdown, columns, button, rerun,
                       write)

from utils.JHCLoader import jhc_loader


def window_setter() -> None:
    """ Set the window configuration.
    :return: None
    """
    # Inject the custom JavaScript, HTML, and CSS for the layout
    # jhc_loader("static/script", "static/index", "static/style")

    # Set page configuration
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
    # Set the layout for the welcome message and the logout button
    left, right = columns([6, 1], gap="small", vertical_alignment="center")
    with left:
        # Display the welcome message
        markdown(
            f"""
            <div style="display: flex; align-items: center; padding: 0.5rem 1rem; border-radius: 8px;">
                <span style="font-size: 1.5rem;">
                👋 Welcome, <strong>{session_state["username"]}</strong> ：）
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )
    with right:
        # Display the logout button
        if button("Logout", type="primary", icon=":material/logout:", use_container_width=True):
            # Clear the session state to log out the user
            session_state.clear()
            rerun()

    # Set the structure of the sidebar navigation
    pages: dict = {
        "page": [
            "subpages/home.py",
            "subpages/account.py",
            "subpages/database.py",
            "subpages/display.py",
            "subpages/trade.py",
            "subpages/analysis.py",
            "subpages/about.py",
        ],
        "title": [
            "Home",
            "Account",
            "Database Creation & Management",
            "Data Generate, Display & Insert",
            "Data Trade",
            "Post-Trade Data Analysis",
            "About",
        ],
        "icon": [
            ":material/home:",
            ":material/account_circle:",
            ":material/database:",
            ":material/table_view:",
            ":material/currency_exchange:",
            ":material/robot:",
            ":material/info:",
        ],
    }

    structure: dict = {
        "Introduction": [
            Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
        ],
        "Core Functions": [
            Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
            Page(page=pages["page"][2], title=pages["title"][2], icon=pages["icon"][2]),
            Page(page=pages["page"][3], title=pages["title"][3], icon=pages["icon"][3]),
            Page(page=pages["page"][4], title=pages["title"][4], icon=pages["icon"][4]),
            Page(page=pages["page"][5], title=pages["title"][5], icon=pages["icon"][5]),
        ],
        "Information": [
            Page(page=pages["page"][6], title=pages["title"][6], icon=pages["icon"][6]),
        ],
    }
    pg = navigation(structure, position="sidebar", expanded=True)
    pg.run()


def sidebar_hider():
    markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
