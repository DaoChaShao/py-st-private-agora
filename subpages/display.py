#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/20 22:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   display.py
# @Desc     :   

from streamlit import (sidebar, subheader, selectbox, caption, empty,
                       button, slider, spinner, session_state, rerun)
from os import path
from pandas import DataFrame

from utils.DB import (generator_social_media,
                      generator_short_video,
                      generator_mobile_payment,
                      generator_health_fitness,
                      generator_maps_navigation,
                      query_executor,
                      data_exists_checker)
from utils.helper import Timer, SeedSetter

empty_messages: empty = empty()
empty_data: empty = empty()

# Initialise the session state for the data
for key in [
    "social_media",
    "short_video",
    "mobile_payment",
    "health_fitness",
    "maps_navigation"
]:
    if key not in session_state:
        session_state[key] = []

if path.exists("db_sqlite.db"):
    with sidebar:
        subheader("Data Categories")
        # Set the data number in the sidebar
        number: int = slider(
            "Select the Number of Data Points",
            min_value=10, max_value=100, value=20, step=1,
            help="Choose the number of data points to display in the application."
        )
        caption(f"The number you select is **{number}**.")

        # Set the data duration in the sidebar
        weeks: list[int] = [7, 14, 21, 28]
        week: int = selectbox(
            "Select the Duration of Data",
            weeks, index=0,
            help="Choose the duration for which you want to generate data."
        )
        match week:
            case 7:
                week_num: int = 1
            case 14:
                week_num: int = 2
            case 21:
                week_num: int = 3
            case _:
                week_num: int = 4
        caption(f"The duration you selected is **{week_num}** week.")

        # Set the data number in the sidebar
        categories: list[str] = ["Social Media", "Short Video", "Mobile Payment", "Health & Fitness",
                                 "Maps & Navigation"]
        category: str = selectbox(
            "Select a Category of the Data",
            ["Select a category"] + categories, index=0,
            help="Choose a category to explore the data available in this section."
        )
        if category != "Select a category":
            caption(f"The category you selected is **{category}**.")
            empty_messages.info(f"Here you can explore the data related to **{category}**.")

            # Initialise the session state for data insert
            if "inserted_status" not in session_state:
                session_state.inserted_status = {
                    category: data_exists_checker(category)
                    for category in [
                        "Social Media",
                        "Short Video",
                        "Mobile Payment",
                        "Health & Fitness",
                        "Maps & Navigation"
                    ]
                }
            button_status = session_state.inserted_status.get(category, False)
            # Initialise the session state for the inserted message display
            if "message_status" not in session_state:
                session_state.message_status = False
            if "message_success" not in session_state:
                session_state.message_success = ""
            if "category_generate" not in session_state:
                session_state.category_generate = None

            if button(
                    "Generate & Show Category Data", type="primary", use_container_width=True,
                    help="Click to display the data in this category."
            ):

                # Check if the data for the selected category has been generated
                session_state.category_generate = category

                with spinner():
                    empty_messages.info("Generating data, please wait...")

                    # Generate and display the data based on the selected category
                    match category:
                        case "Social Media":
                            with Timer("Generating & Displaying **SOCIAL MEDIA**", precision=3) as timer:
                                with SeedSetter():
                                    session_state.social_media = generator_social_media(number, week)
                                    # Flatten the data structure for display
                                    flat: list[dict] = [
                                        {
                                            **day, "category": user["category"], "price": user["price"],
                                            "gender": user["gender"], "age": user["age"],
                                            "create_time": user["create_time"],
                                        }
                                        for user in session_state.social_media
                                        for day in user["content"]
                                    ]
                                    empty_data.data_editor(
                                        DataFrame(flat),
                                        disabled=True,
                                        hide_index=True,
                                        use_container_width=True,
                                        height=525
                                    )
                            empty_messages.success(timer)
                        case "Short Video":
                            with Timer("Generating & Displaying **SHORT VIDEO**", precision=3) as timer:
                                with SeedSetter():
                                    session_state.short_video = generator_short_video(number, week)
                                    # Flatten the data structure for display
                                    flat: list[dict] = [
                                        {
                                            **day, "category": user["category"], "price": user["price"],
                                            "gender": user["gender"], "age": user["age"],
                                            "create_time": user["create_time"],
                                        }
                                        for user in session_state.short_video
                                        for day in user["content"]
                                    ]
                                    empty_data.data_editor(
                                        DataFrame(flat),
                                        disabled=True,
                                        hide_index=True,
                                        use_container_width=True,
                                        height=525
                                    )
                            empty_messages.success(timer)
                        case "Mobile Payment":
                            with Timer("Generating & Displaying **MOBILE PAYMENT**", precision=3) as timer:
                                with SeedSetter():
                                    session_state.mobile_payment = generator_mobile_payment(number, week)
                                    # Flatten the data structure for display
                                    flat: list[dict] = [
                                        {
                                            **day, "category": user["category"], "price": user["price"],
                                            "gender": user["gender"], "age": user["age"],
                                            "create_time": user["create_time"],
                                        }
                                        for user in session_state.mobile_payment
                                        for day in user["content"]
                                    ]
                                    empty_data.data_editor(
                                        DataFrame(flat),
                                        disabled=True,
                                        hide_index=True,
                                        use_container_width=True,
                                        height=525
                                    )
                            empty_messages.success(timer)
                        case "Health & Fitness":
                            with Timer("Generating & Displaying **HEALTH & FITNESS**", precision=3) as timer:
                                with SeedSetter():
                                    session_state.health_fitness = generator_health_fitness(number, week)
                                    # Flatten the data structure for display
                                    flat: list[dict] = [
                                        {
                                            **day, "category": user["category"], "price": user["price"],
                                            "gender": user["gender"], "age": user["age"],
                                            "create_time": user["create_time"],
                                        }
                                        for user in session_state.health_fitness
                                        for day in user["content"]
                                    ]
                                    empty_data.data_editor(
                                        DataFrame(flat),
                                        disabled=True,
                                        hide_index=True,
                                        use_container_width=True,
                                        height=525
                                    )
                            empty_messages.success(timer)
                        case "Maps & Navigation":
                            with Timer("Generating & Displaying **MAPS & NAVIGATION**", precision=3) as timer:
                                with SeedSetter():
                                    session_state.maps_navigation = generator_maps_navigation(number, week)
                                    # Flatten the data structure for display
                                    flat: list[dict] = [
                                        {
                                            **day, "category": user["category"], "price": user["price"],
                                            "gender": user["gender"], "age": user["age"],
                                            "create_time": user["create_time"],
                                        }
                                        for user in session_state.maps_navigation
                                        for day in user["content"]
                                    ]
                                    empty_data.data_editor(
                                        DataFrame(flat),
                                        disabled=True,
                                        hide_index=True,
                                        use_container_width=True,
                                        height=525
                                    )
                            empty_messages.success(timer)
                        case _:
                            empty_messages.warning(f"Data for **{category}** is not yet available.")

            # Set the button to insert the data into the database
            if session_state.category_generate == category:
                if button(
                        "Insert Data", type="secondary", use_container_width=True,
                        disabled=button_status,
                        help="Click to insert the displayed data into the SQLite database."
                ):
                    if path.exists("db_sqlite.db"):
                        with spinner("Inserting data into the database..."):
                            # Implement the logic to insert the data into your database
                            match category:
                                case "Social Media":
                                    for user in session_state.social_media:
                                        query_executor(user)
                                        session_state.message_success = "Data **SOCIAL MEDIA** is inserted successfully!"
                                        session_state.message_status = True
                                        session_state.inserted_status["Social Media"] = True
                                case "Short Video":
                                    for user in session_state.short_video:
                                        query_executor(user)
                                        session_state.message_success = "Data **SHORT VIDEO** is inserted successfully!"
                                        session_state.message_status = True
                                        session_state.inserted_status["Short Video"] = True
                                case "Mobile Payment":
                                    for user in session_state.mobile_payment:
                                        query_executor(user)
                                        session_state.message_success = "Data **MOBILE PAYMENT** is inserted successfully!"
                                        session_state.message_status = True
                                        session_state.inserted_status["Mobile Payment"] = True
                                case "Health & Fitness":
                                    for user in session_state.health_fitness:
                                        query_executor(user)
                                        session_state.message_success = "Data **HEALTH & FITNESS** is inserted successfully!"
                                        session_state.message_status = True
                                        session_state.inserted_status["Health & Fitness"] = True
                                case "Maps & Navigation":
                                    for user in session_state.maps_navigation:
                                        query_executor(user)
                                        session_state.message_success = "Data **MAPS & NAVIGATION** is inserted successfully!"
                                        session_state.message_status = True
                                        session_state.inserted_status["Maps & Navigation"] = True
                                case _:
                                    empty_messages.error(f"Data for **{category}** is not yet available.")
                            # Refresh the page to update the session state
                            rerun()
                    else:
                        empty_messages.error(f"Data inserted into the database does not exist.")

                # Display the success message if the data is inserted successfully.
                if session_state.message_status:
                    empty_messages.success(session_state.message_success)
                    session_state.message_status = False
                    session_state.category_generate = None

        else:
            caption("You must select a category to display the data.")
            empty_messages.info("Please **select a category** to explore the data.")
else:
    empty_messages.error("You must create SQLite database firstly.")
