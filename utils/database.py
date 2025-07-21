#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/20 23:45
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   database.py
# @Desc     :   

from datetime import datetime, timedelta
from faker import Faker
from random import choice, randint, uniform, sample

# Initialise Faker to generate random data
fake = Faker("zh_CN")

# General constants
GENDERS: list[str] = ["male", "female"]
DEVICE_TYPES: list[str] = ["IOS", "Android", "Web", "Wearable"]
LOCATIONS: list[str] = [
    # Provinces: 23
    "Hebei", "Shanxi", "Liaoning", "Jilin", "Heilongjiang", "Jiangsu",
    "Zhejiang", "Anhui", "Fujian", "Jiangxi", "Shandong", "Henan",
    "Hubei", "Hunan", "Guangdong", "Hainan", "Sichuan", "Guizhou",
    "Yunnan", "Shaanxi", "Gansu", "Qinghai", "Taiwan",
    # Autonomous Regions: 5
    "Inner Mongolia", "Guangxi", "Tibet", "Ningxia", "Xinjiang",
    # Municipalities: 4
    "Beijing", "Tianjin", "Shanghai", "Chongqing",
    # Special Administrative Regions (SAR): 2
    "Hong Kong", "Macau"
]
TOPICS: list[str] = [
    "Comedy/Skits", "Food & Restaurants", "Fashion & Outfit", "Fitness & Sports", "Dance & Talent",
    "Travel & Scenery", "Emotional & Motivation", "Pets & Animals", "Parenting & Family", "Tech & Science",
    "Gaming & Commentary", "Movie/TV Clips", "Campus Life", "Workplace Tips", "Life Hacks",
    "Car Reviews", "Short Drama / Story", "Beauty & Selfie", "Music & Singing", "Zodiac & Tarot",
    "DIY & Crafts", "Traditional Culture", "News & Current Affairs", "Product Recommendation", "Livestream Highlights"
]

# Social media constants
PLATFORMS: list[str] = ["TikTok", "Douyin", "Red Note", "Instagram", "YouTube Shorts", "Kuaishou", "Facebook", "X"]

# Mobile Payment constants
PAYMENT_TYPES: list[str] = ["WeChat Pay", "Alipay", "Apple Pay", "Google Pay", "Credit Card", "Debit Card", "Coupon"]
TRANSACTION_TYPES: list[str] = [
    "Dining", "Transportation", "Entertainment", "Shopping", "Medical",
    "Education", "Communication", "Accommodation", "Life Services", "Beauty & Hairdressing",
    "Finance & Investment", "Automotive Services", "Electronics",
]

# Health & Fitness constants
EQUIPMENTS: list[str] = ["Smartphone", "Smartwatch", "Fitness Band", "Tablet"]
WORKOUT_TYPES: list[str] = ["Cardio", "Strength Training", "Yoga", "Pilates", "HIIT", "Cycling", "Running", "Walking"]
ENVIRONMENTS: list[str] = ["Gym", "Home", "Outdoor Park", "Studio", "Office"]

# Maps & Navigation constants
TRANSPORT_MODES: list[str] = ["walking", "driving", "cycling", "public_transport", "scooter"]
NAVIGATION_PURPOSES: list[str] = ["commute", "travel", "shopping", "exercise", "visit"]
FREQUENT_DESTINATION: list[str] = ["restaurant", "office", "coffee shop", "gym", "park", "home", "mall", "hospital"]


def generator_social_media(user_num: int = 2, days: int = 7, start_date: str = "2025-01-01") -> list:
    """ Generate simulated social media user behaviour data.
    :param user_num: Number of the number of users
    :param days: The number of days per user
    :param start_date: Starting date (YYYY-MM-DD)
    :return: List of user data dictionaries
    """
    # Set the base date for data generation
    base_date = datetime.strptime(start_date, "%Y-%m-%d")

    # Initialise a list to hold data for each user
    users_data = []
    for _ in range(user_num):
        gender: str = choice(GENDERS)
        age: int = randint(18, 65)

        # Generate data for each day of the week for the user
        weekly_log = []
        for i in range(days):
            # Generate random data for each day
            daily_log = {
                "date": (base_date + timedelta(days=i)).strftime("%Y-%m-%d"),
                "platform": sample(PLATFORMS, randint(1, 3)),
                "topics": sample(TOPICS, k=randint(1, 5)),
                "total_watch_time(min)": randint(1, 180),
                "likes": randint(1, 500),
                "comments": randint(1, 200),
                "collects": randint(1, 300),
                "shares": randint(1, 100),
                "longest_single_watch_duration(min)": randint(1, 30),
                "peak_watch_time": randint(0, 23),
                "locations": sample(LOCATIONS, k=randint(1, 3)),
                "device": choice(DEVICE_TYPES),
                "payment_method": sample(PAYMENT_TYPES, randint(1, 3)),
            }
            weekly_log.append(daily_log)

        users_data.append({
            "gender": gender,
            "age": age,
            "weekly_log": weekly_log
        })

    return users_data


def generator_short_video(user_num: int = 2, days: int = 7, start_date: str = "2025-01-01") -> list:
    """ Generate short video behaviour data for multiple users over multiple days.
    :param user_num: The number of users to generate data for
    :param days: The number of days for which to generate data (default is 7) is
    :param start_date: The start date for the data generation in "YYYY-MM-DD" format
    :return: Each containing a list of dictionaries with user data for each day
    """
    # Set the base date for data generation
    base_date = datetime.strptime(start_date, "%Y-%m-%d")

    # Initialise a list to hold data for each user
    users_data = []
    for _ in range(user_num):
        gender: str = choice(GENDERS)
        age: int = randint(18, 65)

        # Generate data for each day of the week for the user
        weekly_behaviour = []
        for i in range(days):
            # Generate random data for each day
            daily_behaviour = {
                "date": (base_date + timedelta(days=i)).strftime("%Y-%m-%d"),
                "video_type": sample(TOPICS, k=randint(1, 5)),
                "total_watch_time(min)": randint(1, 180),
                "likes": randint(1, 500),
                "comments": randint(1, 200),
                "collects": randint(1, 300),
                "shares": randint(1, 100),
                "longest_single_watch_duration(min)": randint(1, 30),
                "peak_watch_time": randint(0, 23),
                "locations": sample(LOCATIONS, k=randint(1, 3)),
                "device": choice(DEVICE_TYPES),
                "payment_method": sample(PAYMENT_TYPES, randint(1, 3)),
            }
            weekly_behaviour.append(daily_behaviour)

        users_data.append({
            "gender": gender,
            "age": age,
            "weekly_behaviour": weekly_behaviour
        })

    return users_data


def generator_mobile_payment(user_num: int = 2, days: int = 7, start_date: str = "2025-01-01") -> list:
    """ Generate data for multiple users weekly.
    :param user_num: The number of users to generate data for
    :param days: The number of days for which to generate data (default is 7) is
    :param start_date: The start date for the data generation in "YYYY-MM-DD" format
    :return: Each containing a list of dictionaries with user data for each day
    """

    base_date = datetime.strptime(start_date, "%Y-%m-%d")

    # Initialise a list to hold data for each user
    users_data = []
    for _ in range(user_num):
        gender: str = choice(GENDERS)
        age: int = randint(18, 65)

        # Generate data for each day of the week for the user
        weekly_data = []
        for i in range(days):
            # Generate random data for each day
            total_transactions: int = randint(1, 25)
            total_amount: float = round(uniform(100, 3000), 2)

            daily_data: dict[str, str | int | float] = {
                "date": (base_date + timedelta(days=i)).strftime("%Y-%m-%d"),
                "total_transactions": total_transactions,
                "total_amount": total_amount,
                "average_expenditure": round(total_amount / total_transactions, 2),
                "peak_period": randint(0, 23),

                "payment_device": choice(DEVICE_TYPES),
                "payment_type": sample(PAYMENT_TYPES, randint(1, 3)),
                "transaction_type": sample(TRANSACTION_TYPES, randint(2, 5)),
                "locations_distribution": sample(LOCATIONS, randint(2, 5)),
            }
            weekly_data.append(daily_data)

        users_data.append({
            "gender": gender,
            "age": age,
            "weekly_data": weekly_data,
        })

    return users_data


def generator_health_fitness(user_num: int = 2, days: int = 7, start_date: str = "2025-01-01") -> list:
    """ Generate health and fitness data for multiple users over a week.
    :param user_num: Number of users
    :param days: The number of days to simulate
    :param start_date: Start date of the simulation (format "YYYY-MM-DD")
    :return: List of user health and fitness activity data
    """
    # Set the base date for data generation
    base_date = datetime.strptime(start_date, "%Y-%m-%d")

    # Initialise a list to hold data for each user
    users_data = []
    for _ in range(user_num):
        gender = choice(GENDERS)
        age = randint(18, 65)

        # Generate data for each day of the week for the user
        weekly_data = []
        for i in range(days):
            # Generate random data for each day
            daily_data: dict[str, str | int | float] = {
                "date": (base_date + timedelta(days=i)).strftime("%Y-%m-%d"),
                "workout_duration(min)": randint(20, 120),
                "calories_burned(kcal)": round(uniform(150, 1000), 2),
                "step_count": randint(300, 20000),
                "average_heart_rate": randint(40, 150),
                "peak_workout_hour": randint(5, 22),
                "equipment": choice(EQUIPMENTS),
                "workout_types": sample(WORKOUT_TYPES, randint(1, 3)),
                "exercise_environment": sample(ENVIRONMENTS, randint(1, 2)),
                "locations": sample(LOCATIONS, randint(1, 2)),
            }
            weekly_data.append(daily_data)

        users_data.append({
            "gender": gender,
            "age": age,
            "weekly_data": weekly_data,
        })

    return users_data


def generator_maps_navigation(user_num: int = 2, days: int = 7, start_date: str = "2025-01-01") -> list:
    """ Generate navigation data for multiple users over a given number of days.
    :param user_num: Number of users to simulate
    :param days: The number of days to generate data for
    :param start_date: The start date (YYYY-MM-DD)
    :return: List of user navigation data
    """
    # Set the base date for data generation
    base_date = datetime.strptime(start_date, "%Y-%m-%d")

    # Initialise a list to hold data for each user
    users_data = []
    for _ in range(user_num):
        gender = choice(GENDERS)
        age = randint(18, 65)

        # Generate data for each day of the week for the user
        weekly_usage = []
        for i in range(days):
            # Generate random data for each day
            total_distance: float = round(uniform(2.0, 50.0), 2)
            total_time = round(uniform(10.0, 180.0), 2)

            daily_usage = {
                "date": (base_date + timedelta(days=i)).strftime("%Y-%m-%d"),
                "total_trips": randint(1, 5),
                "total_distance(km)": total_distance,
                "total_navigation_time(min)": total_time,
                "average_speed(km/h)": round(total_distance / (total_time / 60), 2) if total_time > 0 else 0,
                "peak_navigation_hour": randint(6, 22),
                "transport_modes": sample(TRANSPORT_MODES, randint(1, 3)),
                "navigation_purposes": sample(NAVIGATION_PURPOSES, randint(1, 3)),
                "device": choice(DEVICE_TYPES),
                "frequent_destinations": sample(FREQUENT_DESTINATION, randint(2, 4)),
            }

            weekly_usage.append(daily_usage)

        users_data.append({
            "gender": gender,
            "age": age,
            "weekly_usage": weekly_usage,
        })

    return users_data
