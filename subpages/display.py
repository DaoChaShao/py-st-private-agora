#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/20 22:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   display.py
# @Desc     :   

from streamlit import (sidebar, subheader, selectbox, caption, empty,
                       button, slider, spinner, )

from utils.database import (generator_social_media,
                            generator_short_video, )
from utils.helper import Timer, SeedSetter

empty_messages: empty = empty()
empty_data: empty = empty()

with sidebar:
    subheader("Data Categories")
    # Set the data number in the sidebar
    number: int = slider(
        "Select the Number of Data Points",
        min_value=100, max_value=1000, value=200, step=1,
        help="Choose the number of data points to display in the application."
    )
    caption(f"The number you select is {number}.")
    # Set the data number in the sidebar
    categories = ["Social Media", "Short Video", "Mobile Payment", "Health & Fitness ", "Maps & Navigation"]
    category: str = selectbox(
        "Select a Category of the Data",
        ["Select a category"] + categories, index=0,
        help="Choose a category to explore the data available in this section."
    )
    if category != "Select a category":
        caption(f"The category you selected is {category}.")
        empty_messages.info(f"Here you can explore the data related to **{category}**.")
        if button(
                "Display", type="primary", use_container_width=True,
                help="Click to display the data in this category."
        ):
            with spinner():
                empty_messages.info("Generating data, please wait...")

                # Generate and display the data based on the selected category
                match category:
                    case "Social Media":
                        with Timer("Generating & Displaying **social media**", precision=3) as timer:
                            with SeedSetter():
                                data = generator_social_media(number)
                                empty_data.data_editor(
                                    data,
                                    disabled=True,
                                    hide_index=True,
                                    use_container_width=True,
                                    height=525
                                )
                        empty_messages.success(timer)
                    case "Short Video":
                        with Timer("Generating & Displaying **short video**", precision=3) as timer:
                            with SeedSetter():
                                data = generator_short_video(number)
                                empty_data.data_editor(
                                    data,
                                    disabled=True,
                                    hide_index=True,
                                    use_container_width=True,
                                    height=525
                                )
                        empty_messages.success(timer)
                    case _:
                        empty_messages.warning(f"Data for **{category}** is not yet available.")
    else:
        caption("You must select a category to display the data.")
        empty_messages.info("Please **select a category** to explore the data.")
