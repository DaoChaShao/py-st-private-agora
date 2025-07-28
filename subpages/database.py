#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/25 00:06
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   DB.py
# @Desc     :

from json import loads
from os import path
from pandas import DataFrame
from streamlit import (sidebar, subheader, empty, text_input, button,
                       caption, spinner, session_state, rerun)
from textwrap import dedent

from utils.DB import (SQLiteInitializer,
                      is_db, db_remover)

empty_messages: empty = empty()

# Statement of the SQLite database execution
STATEMENT_INIT: str = dedent(
    "CREATE TABLE IF NOT EXISTS users ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "gender TEXT NOT NULL,"
    "age INTEGER NOT NULL,"
    "category TEXT NOT NULL,"
    "price REAL NOT NULL,"
    "content TEXT NOT NULL,"
    "created_time TEXT NOT NULL);"
)

STATEMENT_CHECK: str = dedent(
    "SELECT name FROM sqlite_master WHERE type='table';"
)

STATEMENT_DISPLAY: str = dedent(
    "SELECT * FROM users;"
)

with sidebar:
    subheader("Database Management")
    # Create a database such as SQLite
    db_name: str = text_input(
        "The name of the database",
        value="db_sqlite", type="default", disabled=True,
        help="Enter the name of your Database."
    )
    caption("The default database is SQLite, and the name is set to `db_sqlite`.")

    # Check if the database file exists
    if path.exists("db_sqlite.db"):
        empty_messages.info(
            f"The database file `{db_name}` already exists. You can create or delete it if you want."
        )
        if button(
                "Display Database", type="secondary", use_container_width=True,
                help="Click to display the content of the SQLite database with the name `db_sqlite`."
        ):
            with spinner("Displaying the database content..."):
                empty_messages.info("Generating data, please wait...")
                # Display the database content
                with SQLiteInitializer(STATEMENT_DISPLAY) as sqlite:
                    rows = sqlite.table_display()
                    columns = ["id", "gender", "age", "category", "price", "content", "created_time"]
                    flat: list = []
                    if rows:
                        for row in rows:
                            id, gender, age, category, price, content_str, created_time = row
                            content_list: dict = loads(content_str)
                            for content_item in content_list:
                                flat.append({
                                    "id": id,
                                    "gender": gender,
                                    "age": age,
                                    "category": category,
                                    "price": price,
                                    "created_time": created_time,
                                    **content_item,
                                })
                            # Display the table data in the Streamlit app
                            empty_messages.data_editor(
                                DataFrame(flat),
                                disabled=True,
                                hide_index=True,
                                use_container_width=True,
                                height=600,
                            )
                    else:
                        empty_messages.warning("The database is empty.")

        # If the database has been created, you can delete it if you want
        if button(
                "Delete Database", type="tertiary", use_container_width=True,
                help="Click to delete the SQLite database with the name `db_sqlite`."
        ):
            with spinner("Deleting the database..."):
                # Reset the session state
                session_state.db_created = False
                db_remover()
                empty_messages.success(f"The database deleted successfully!")
                rerun()
    else:
        empty_messages.warning("The database has not been created yet.")

        if db_name == "db_sqlite":
            # Check if the database has been created
            if "db_created" not in session_state:
                session_state.db_created = False

            # Create a button to create the database
            if button(
                    "Create Database", type="primary", use_container_width=True,
                    help="Click to create the SQLite database with the name `db_sqlite`.",
            ):
                with spinner("Creating the database..."):
                    # Initialise the SQLite database
                    with SQLiteInitializer(STATEMENT_INIT) as sqlite:
                        session_state.db_created = True
                        empty_messages.success(f"Database `{db_name}` created successfully!")
                # Rerun the app to refresh the state
                rerun()
        else:
            empty_messages.error("Please enter the database name you like.")
