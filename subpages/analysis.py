#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/27 11:19
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   analysis.py
# @Desc     :   

from pandas import DataFrame
from streamlit import (empty, sidebar, subheader, selectbox, caption,
                       slider, text_input, session_state, multiselect,
                       button, spinner, )

from utils.helper import (post_data_categories_getter,
                          post_data_contents_getter,
                          Timer,
                          prompty_generator)
from utils.model import OpenAICompleter, DeepSeekCompleter

empty_messages: empty = empty()
empty_analysis: empty = empty()

if "selected_data" not in session_state:
    session_state.selected_data = None

with sidebar:
    subheader("Data Trading Settings")
    # Set the category of data
    if session_state.selected_data is not None:
        categories: list[str] = post_data_categories_getter(session_state.selected_data)
        category: str = selectbox(
            "Select a Category of the Data",
            ["Select a category"] + categories, index=0,
            help="Choose a category of data to be ready to trade."
        )
        if category != "Select a category":
            caption(f"The category you selected is **{category}**.")

            languages: list[str] = ["English", "Chinese", "French", "Russian"]
            language: str = selectbox(
                "Select a Language",
                languages, index=0,
                help="Choose a language for data analysis. The model will respond in the selected language."
            )

            models: list[str] = ["OpenAI", "DeepSeek"]
            model: str = selectbox(
                "Select a Large Language Model",
                ["Select a model"] + models, index=0,
                help="Choose a large language model to be used for data analysis."
            )
            if model != "Select a model":
                caption(f"The model you selected is **{model}**.")

                match model:
                    case "OpenAI":
                        subheader("OpenAI Parameters")
                        temperature: float = slider(
                            "Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1, disabled=True,
                            help="Controls the randomness of the model's output. Lower values make it more deterministic.",
                        )
                        Top_p: float = slider(
                            "Top-p", min_value=0.0, max_value=1.0, value=0.9, step=0.1, disabled=True,
                            help="Controls the diversity of the model's output by sampling from the top p% of the probability distribution.",
                        )
                        model: str = selectbox(
                            "OpenAi Model", ["gpt-3.5-turbo"], index=0, disabled=True,
                            help="Select the OpenAI model to use.",
                        )
                        api_key: str = text_input(
                            "OpenAI API Key",
                            max_chars=164, type="password",
                            help="OpenAI API key for authentication",
                        )
                        caption(f"The length of API key you entered is {len(api_key)} characters.")
                        if not api_key:
                            empty_messages.error("Please enter your OpenAI API key.")
                        elif api_key and not api_key.startswith("sk-"):
                            empty_messages.error("Please enter a **VALID** OpenAI API key.")
                        elif api_key and api_key.startswith("sk-") and len(api_key) != 164:
                            empty_messages.warning("The length of OpenAI API key should be 164 characters.")
                        elif api_key and api_key.startswith("sk-") and len(api_key) == 164:
                            empty_messages.success("The OpenAI API key is valid.")

                            if button(
                                    "Analyze Data", type="primary", use_container_width=True,
                                    help="Click to analyse the data using the selected model and parameters."
                            ):
                                with Timer("Analyzing Data") as timer:
                                    with spinner("Analyzing Data"):
                                        role: str = (
                                            "You are a professional data analyst with strong skills in data visualization and markdown formatting. "
                                            "You understand pandas DataFrame structures and can interpret them accurately."
                                        )
                                        post_data_details: list[str] = post_data_contents_getter(
                                            session_state.selected_data, category
                                        )
                                        prompt: str = prompty_generator(role, post_data_details, language)
                                        opener = OpenAICompleter(api_key=api_key, temperature=temperature, top_p=Top_p)
                                        response: str = opener.client(content=role, prompt=prompt, model=model)
                                        empty_analysis.markdown(response)
                                empty_messages.success(timer)

                    case "DeepSeek":
                        subheader("DeepSeek Parameters")
                        temperature: float = slider(
                            "Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1, disabled=True,
                            help="Controls the randomness of the model's output. Lower values make it more deterministic.",
                        )
                        model: str = selectbox(
                            "DeepSeek Model", ["deepseek-chat"], index=0, disabled=True,
                            help="Select the DeepSeek model to use.",
                        )
                        api_key: str = text_input(
                            "DeepSeek API Key",
                            max_chars=35, type="password",
                            help="DeepSeek API key for authentication",
                        )
                        caption(f"The length of API key you entered is {len(api_key)} characters.")
                        if not api_key:
                            empty_messages.error("Please enter your DeepSeek API key.")
                        elif api_key and not api_key.startswith("sk-"):
                            empty_messages.error("Please enter a **VALID** DeepSeek API key.")
                        elif api_key and api_key.startswith("sk-") and len(api_key) != 35:
                            empty_messages.warning("The length of DeepSeek API key should be 164 characters.")
                        elif api_key and api_key.startswith("sk-") and len(api_key) == 35:
                            empty_messages.success("The DeepSeek API key is valid.")

                            if button(
                                    "Analyze Data", type="primary", use_container_width=True,
                                    help="Click to analyse the data using the selected model and parameters."
                            ):
                                with Timer("Analyzing Data") as timer:
                                    with spinner("Analyzing Data"):
                                        role: str = "You are a professional data analyst with expertise in data trading and analysis. "
                                        post_data_details: list[str] = post_data_contents_getter(
                                            session_state.selected_data, category
                                        )
                                        prompt: str = prompty_generator(role, post_data_details, language)
                                        seeker = DeepSeekCompleter(api_key=api_key, temperature=temperature)
                                        response: str = seeker.client(content=role, prompt=prompt, model=model)
                                        empty_analysis.markdown(response)
                                empty_messages.success(timer)
                    case _:
                        empty_messages.error(f"Model {model} is not supported yet. Please choose another model.")
            else:
                empty_messages.warning(f"You should choose a model to use.")
        else:
            empty_messages.info(f"You should choose a category of data for analysis.")
    else:
        empty_messages.error(f"You should trade the data initially on the page of **Data Trade**.")
