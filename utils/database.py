#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/20 23:45
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   database.py
# @Desc     :   

from enum import Enum, unique
from faker import Faker
from pandas import DataFrame
from random import choice, randint

# Initialize Faker to generate random data
fake = Faker()


@unique
class Gender(Enum):
    """ Set an interface for gender.
    :param Enum: Enum class
    """
    MALE = "male"
    FEMALE = "female"


def generator_social_media(number: int) -> DataFrame:
    """ Generate random social media data.
    :param number: The number of data points to generate.
    :return: A list of dictionaries containing social media data.
    """
    return DataFrame(
        [
            {
                "gender": choice([Gender.MALE, Gender.FEMALE]).value,
                "post_time": fake.date_time_this_year(),
                "content": fake.sentence(nb_words=randint(10, 30)),
                "likes": randint(1, 1000),
                "comments": randint(1, 500),
                "collects": randint(1, 100),
                "shares": randint(1, 300),
                "location": fake.city(),
                "device": choice(["iOS", "Android", "Web"]),
            }
            for i in range(number)
        ]
    )


def generator_short_video(number: int) -> DataFrame:
    """ Generate random short video data.
    :param number: The number of data points to generate.
    :return: A list of dictionaries containing shor video data.
    """
    return DataFrame(
        [
            {
                "gender": choice([Gender.MALE, Gender.FEMALE]).value,
                "post_time": fake.date_time_this_year(),
                "title": fake.sentence(nb_words=randint(3, 7)),
                "content": fake.sentence(nb_words=randint(10, 30)),
                "likes": randint(1, 1000),
                "comments": randint(1, 500),
                "collects": randint(1, 100),
                "shares": randint(1, 300),
                "views": randint(100, 10000),
                "duration(sec)": randint(5, 300),
                "watch_completion_rate": round(randint(50, 100) / 100, 2),
                "location": fake.city(),
                "device": choice(["iOS", "Android", "Web"]),
            }
            for i in range(number)
        ]
    )
