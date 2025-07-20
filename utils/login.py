#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 17:44
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   login.py
# @Desc     :   

from streamlit import (form, text_input, form_submit_button,
                       columns, empty, session_state, rerun)


def authority_checker() -> bool:
    """ Check the authentication status of the user.
    :return: Bool
    """
    # Initialise the session state for login status if not already set
    # - if "authenticated" in the session state, the result of session state will be True
    # - if not, the result will be False
    if session_state.get("authenticated", False):
        return True

    # Set up the layout for the login form
    left, mid, right = columns([1, 2, 1], gap="small", vertical_alignment="center")

    # Create a form for user login
    with mid:
        # Display the messages for the login form
        empty_messages: empty = empty()

        # Display the login tips
        empty_messages.info("Please enter your username and password.")

        # Create a form with fields for username and password
        with form("login", clear_on_submit=True, enter_to_submit=True, width=600):
            username: str = text_input(
                "Username",
                max_chars=30,
                type="default",
                placeholder="Enter your username",
                help="Please enter your username to access the application.",
            )
            password: str = text_input(
                "Password",
                max_chars=30,
                type="password",
                placeholder="Enter your password",
                help="Please enter your password to access the application.",
            )

            if form_submit_button("Login", type="primary", icon=":material/login:", use_container_width=True):
                if username == "admin" and password == "admin":
                    # If the username and password are correct
                    # - set "authenticated" in the session state
                    # - its value of session state is True
                    session_state["authenticated"] = True
                    # Store the username in the session state
                    session_state["username"] = username
                    rerun()
                elif username == "" and password == "":
                    empty_messages.info("Username and Password cannot be **EMPTY**!")
                elif username != "admin" and password == "admin":
                    empty_messages.warning("**INCORRECT USERNAME**. Please try again.")
                elif username == "admin" and password != "admin":
                    empty_messages.warning("**INCORRECT PASSWORD**. Please try again.")
                else:
                    empty_messages.error("INCORRECT username and password!")
            return False
