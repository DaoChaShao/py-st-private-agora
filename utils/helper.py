#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 16:43
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :

from faker import Faker
from pandas import DataFrame
from random import seed as random_seed, getstate as get_state, setstate as set_state
from time import perf_counter

fake = Faker()


class Timer(object):
    """ timing code blocks using a context manager """

    def __init__(self, description: str = None, precision: int = 5):
        """ Initialise the Timer class
        :param description: the description of a timer
        :param precision: the number of decimal places to round the elapsed time
        """
        self._description: str = description
        self._precision: int = precision
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        """ Start the timer """
        self._start = perf_counter()
        print()
        print("-" * 50)
        print(f"{self._description} has been started.")
        return self

    def __exit__(self, *args):
        """ Stop the timer and calculate the elapsed time """
        self._end = perf_counter()
        self._elapsed = self._end - self._start

    def __repr__(self):
        """ Return a string representation of the timer """
        if self._elapsed != 0.0:
            print("-" * 50)
            return f"{self._description} took {self._elapsed:.{self._precision}f} seconds."
        return f"{self._description} has NOT been started."


class SeedSetter(object):
    """ Set a random seed for reproducibility. """

    def __init__(self, seed: int = 9527):
        """ Initialise the RandomSeed class with a seed. """
        self._seed = seed
        self._state_random = None
        self._state_faker = None

    def __enter__(self):
        """ Enter the context manager and set the random seed. """
        # Store the current state of random and Faker
        self._state_random = get_state()
        self._state_faker = fake.random.getstate()
        # Set the random seed for reproducibility
        random_seed(self._seed)
        Faker.seed(self._seed)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Exit the context manager and reset the random seed. """
        # Reset the random and Faker states to their original values.
        set_state(self._state_random)
        fake.random.setstate(self._state_faker)
        return False

    def __str__(self):
        """ Return a string representation of the random seed. """
        return f"SeedSetter with seed {self._seed}"


def post_data_categories_getter(data: DataFrame) -> list[str]:
    """ Retrieve the unique categories of data from the SQLite database.
    :param data: DataFrame: The DataFrame containing the data
    :return: A list of unique categories
    """
    result = data["category"].unique().tolist()
    print(result)
    return sorted(result)


def post_data_contents_getter(data: DataFrame, category: str) -> DataFrame:
    """ Retrieve the contents of a specific category from the SQLite database.
    :param data: DataFrame: The DataFrame containing the data
    :param category: str: The category to filter by
    :return: A list of contents in the specified category
    """
    result = data[data["category"] == category]
    print(result)
    return result


def prompty_generator(role: str, user_input: list[str], language: str = "English") -> str:
    """ Generate a prompt for the LLM based on user input and role.
    :param role: str: The role of the LLM (e.g., "Data Analyst", "Researcher")
    :param user_input: list[str]: The input data from the user, typically a list
    :param language: str: The language in which the LLM should respond
    :return: str: The generated prompt for the LLM
    """
    # print(type(user_input))
    instruction: str = (
        f"Your task is to analyse the following dataset and generate useful insights based on the user's goal: '{user_input}'. "
        f"You should respond in {language}. The output must be in **Markdown** format and contain the following:\n"
        "- A high-level summary of the dataset (e.g., number of rows/columns, types of features)\n"
        "- Key trends or insights (e.g., distributions, anomalies, correlations)\n"
        "- (Optional but preferred) Visual representations using Markdown-compatible syntax, such as:\n"
        "  - Text-based tables (e.g., top 5 rows)\n"
        "  - Bullet lists or headings to structure information\n"
        "  - Text-based bar plots or histograms if useful\n"
        "- Keep the tone professional and neutral. Avoid assumptions or opinions.\n"
        "- Limit to 300 words unless otherwise instructed.\n"
        "- Do NOT add greetings, sign-offs or irrelevant information."
    )
    constraints: str = (
        f"Your response should be professional, analytical, and well-structured. "
        f"Write the response in {language}. "
        f"Avoid personal opinions or assumptions beyond the data. "
        f"Limit the response to between 300 and 500 words. "
        f"Do not include any closing words like 'best regards'. Only return the analysis body in Markdown format."
    )
    content_data = "\n".join(user_input)
    prompt: str = (
        f"{role}\n\n"
        f"The following is a list of content data extracted from user transactions on a trade platform. "
        f"Please analyse it thoroughly:\n\n"
        f"{content_data}\n\n"
        f"{instruction}\n"
        f"{constraints}"
    )
    return prompt
