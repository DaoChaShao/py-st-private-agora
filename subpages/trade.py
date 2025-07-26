#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/20 22:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   trade.py
# @Desc     :   

from os import path
from pandas import DataFrame
from streamlit import (sidebar, subheader, empty, number_input, selectbox,
                       caption, button, spinner, columns, metric)

from utils.DB import (price_getter,
                      data_knapsack_solver,
                      selected_data_filter,
                      flat_data_display, )

empty_messages: empty = empty()
left, right = columns([1, 1], gap="large", vertical_alignment="center")
empty_table_selected: empty = empty()
empty_table_flat: empty = empty()
empty_description_title: empty = empty()
empty_description_p1: empty = empty()
empty_description_P2: empty = empty()
empty_description_p3: empty = empty()

STATEMENT_DISPLAY: str = "SELECT * FROM users;"

with sidebar:
    subheader("Data Trading Settings")
    # Set the category of data
    categories: list[str] = ["Social Media", "Short Video", "Mobile Payment", "Health & Fitness", "Maps & Navigation"]
    category: str = selectbox(
        "Select a Category of the Data",
        ["Select a category"] + categories, index=0,
        help="Choose a category of data to be ready to trade."
    )
    if category != "Select a category":
        caption(f"The category you selected is **{category}**.")

        # Display a description of the selected category
        empty_description_title.subheader("**Data Description**")
        match category:
            case "Social Media":
                empty_description_p1.markdown("- Data comes from user behavior on social media platforms.")
                empty_description_P2.markdown("- Fields: watch duration, likes, comments, shares, device used, etc.")
                empty_description_p3.markdown("- Applicable for user profiling, content recommendation, etc.")
            case "Short Video":
                empty_description_p1.markdown("- Data comes from user behavior on short video platforms.")
                empty_description_P2.markdown("- Fields: video type, watch duration, single watch duration, etc.")
                empty_description_p3.markdown("- Applicable for content recommendation, and advertising, etc.")
            case "Mobile Payment":
                empty_description_p1.markdown("- Data comes from mobile payment platforms.")
                empty_description_P2.markdown("- Fields: payment device, payment method, transaction type, etc.")
                empty_description_p3.markdown("- Applicable for financial profiling, consumption capability analysis.")
            case "Health & Fitness":
                empty_description_p1.markdown("- Data comes from user activities on health and fitness applications.")
                empty_description_P2.markdown("- Fields: exercise duration, calories burned, steps, etc.")
                empty_description_p3.markdown("- Applicable for health management and fitness plan development.")
            case "Maps & Navigation":
                empty_description_p1.markdown("- Data comes from user activities on maps and navigation applications.")
                empty_description_P2.markdown("- Fields: travel frequency, total distance, navigation time, etc.")
                empty_description_p3.markdown("- Applicable for travel planning and traffic analysis.")
            case _:
                empty_description_p1.markdown("No description available for this category.")

        empty_messages.info("Please set your budget and click the trade button to proceed with the trading process.")

        # Set your budget
        budget: int = number_input(
            "Set Your Budget",
            min_value=100, max_value=10000, value=1000, step=100,
            help="Set the budget you want to allocate for trading data."
        )
        caption(f"Your budget is set to **${budget}**.")

        # Set the action for trading
        if button(
                "Trade", type="primary", use_container_width=True,
                help="Click to initiate the trading process for the selected data category."
        ):
            # Get the price list from the users table in the SQLite database
            if path.exists("db_sqlite.db"):
                with spinner("Fetching data prices, please wait..."):
                    prices: list[int] = price_getter()
                    # Display the prices in a table format
                    # if prices:
                    #     empty_table.data_editor(
                    #         DataFrame({"Price": prices}),
                    #         disabled=True,
                    #         hide_index=False,
                    #         use_container_width=True,
                    #         height=320,
                    #     )
                    count, selected_indices, balance = data_knapsack_solver(prices, budget)
                    if count > 0:
                        empty_messages.success(f"Successful! {count} data items within your budget of ${budget}.")
                        # empty_table.data_editor(
                        #     DataFrame({"Price": prices}),
                        #     disabled=True,
                        #     hide_index=False,
                        #     use_container_width=True,
                        #     height=320,
                        # )
                        selected_data = selected_data_filter(STATEMENT_DISPLAY, selected_indices)
                        if not selected_data.empty:
                            with left:
                                metric(
                                    "Data Trading Result",
                                    f"$ {budget - balance}",
                                    delta=f"$ {balance} left in budget",
                                )
                            with right:
                                metric(
                                    "Data Items Selected",
                                    f"{count} items",
                                    delta=f"{count / len(prices) * 100:.2f}% of total items",
                                )
                            empty_table_selected.data_editor(
                                DataFrame(selected_data),
                                disabled=True,
                                hide_index=True,
                                use_container_width=True,
                            )
                            flat = flat_data_display(selected_data)
                            empty_table_flat.data_editor(
                                DataFrame(flat),
                                disabled=True,
                                hide_index=True,
                                use_container_width=True,
                            )
                        else:
                            empty_messages.warning("No data items found for the selected indices.")
                    else:
                        empty_messages.warning("Failed! You cannot buy any data items within your budget of ${budget}.")
            else:
                empty_messages.error(f"The database is not found, please create the database first.")
    else:
        caption("No category selected.")
        empty_messages.info("Please select a category for checking its description.")
