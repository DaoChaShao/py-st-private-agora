#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/20 23:45
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   DB.py
# @Desc     :   

from datetime import datetime, timedelta
from faker import Faker
from json import dumps, loads
from os import path, remove
from pandas import DataFrame, read_sql_query, json_normalize
from random import choice, randint, uniform, sample
from sqlite3 import connect

# Initialise Faker to generate random data
fake = Faker()

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


def generator_social_media(user_num: int = 2, days: int = 7, start_date: str = "2024-01-01") -> list:
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

        # Offer a price for the user's weekly social media data
        price: int = round(randint(50, 300), 2)

        users_data.append({
            "gender": gender,
            "age": age,
            "category": "social media",
            "price": price,
            "content": weekly_log,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

    return users_data


def generator_short_video(user_num: int = 2, days: int = 7, start_date: str = "2023-01-01") -> list:
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

        # Offer a price for the user's weekly short video data
        price: int = round(randint(50, 300), 2)

        users_data.append({
            "gender": gender,
            "age": age,
            "category": "short video",
            "price": price,
            "content": weekly_behaviour,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

    return users_data


def generator_mobile_payment(user_num: int = 2, days: int = 7, start_date: str = "2022-01-01") -> list:
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

        # Offer a price for the user's weekly mobile payment data
        price: int = round(randint(50, 300), 2)

        users_data.append({
            "gender": gender,
            "age": age,
            "category": "mobile payment",
            "price": price,
            "content": weekly_data,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

    return users_data


def generator_health_fitness(user_num: int = 2, days: int = 7, start_date: str = "2021-01-01") -> list:
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

        # Offer a price for the user's weekly health and fitness data
        price: int = round(randint(50, 300), 2)

        users_data.append({
            "gender": gender,
            "age": age,
            "category": "health & fitness",
            "price": price,
            "content": weekly_data,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

    return users_data


def generator_maps_navigation(user_num: int = 2, days: int = 7, start_date: str = "2020-01-01") -> list:
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

        # Offer a price for the user's weekly navigation data
        price: int = round(randint(50, 300), 2)

        users_data.append({
            "gender": gender,
            "age": age,
            "category": "maps & navigation",
            "price": price,
            "content": weekly_usage,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

    return users_data


class SQLiteInitializer(object):
    """ A class to initialise the SQLite database. """

    def __init__(self, statement: str, db_name: str = "db_sqlite") -> None:
        """ Initialise the SQLite database with the given execution command.
        :param statement: The SQL command to execute for initialising the database
        :param db_name: The name of the database file (default is "db_sqlite.db")
        """
        self._statement = statement
        self._db: str = f"{db_name}.db"
        self._connection = None
        self._cursor = None

    def __enter__(self):
        """ Establish and return the database connection when entering the context. """
        # Establish a connection to the SQLite database
        self._connection = connect(self._db)
        # Set the cursor for executing SQL commands
        self._cursor = self._connection.cursor()
        # Execute the provided SQL command
        self._cursor.execute(self._statement)
        # Commit the changes to the database
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Commit and close the database connection when exiting the context."""
        # Commit the changes and close the connection
        if self._connection:
            self._connection.commit()
            self._connection.close()
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return False

    def table_display(self) -> list:
        """ Retrieve the list of tables in the SQLite database.
        :return: A list of table names in the database
        """
        self._cursor.execute(self._statement)
        return self._cursor.fetchall()

    def __str__(self):
        """ Return a string representation of the SQLiteInitializer instance. """
        return f"SQLiteInitializer(db_name={self._db}, statement={self._statement})"


def is_db(statement: str, db_name: str = "db_sqlite") -> bool:
    """ Check if the SQLite database exists.
    :param statement: The SQL command to check for the existence of tables
    :param db_name: The name of the database file (default is "db_sqlite")
    :return: True if the database exists, False otherwise
    """
    with connect(f"{db_name}.db") as connection:
        cursor = connection.cursor()
        cursor.execute(statement)
        tables = cursor.fetchall()
        return len(tables) > 0


def db_remover(db_name: str = "db_sqlite"):
    """ Remove the SQLite database file if it exists.
    :param db_name: The name of the database file to remove (default is "db_sqlite")
    :return: None
    """
    if path.exists(f"{db_name}.db"):
        # Connect to the database and delete all records from the 'users' table
        with connect(f"{db_name}.db") as connection:
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS users;")
            connection.commit()

        # Remove the database file
        remove(f"{db_name}.db")


def query_executor(user: dict, db_name: str = "db_sqlite"):
    """ Execute a custom SQL query on the SQLite database.
    :return: None
    """
    connection = connect(f"{db_name}.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (gender, age, category, price, content, created_time) VALUES (?, ?, ?, ?, ?, ?)",
                   (
                       user["gender"],
                       user["age"],
                       user["category"],
                       user["price"],
                       dumps(user["content"], ensure_ascii=False),
                       user["create_time"],
                   ))
    connection.commit()
    connection.close()


def price_getter(db_name: str = "db_sqlite") -> list[int]:
    """ Retrieve the prices of all users from the SQLite database.
    :param db_name: The name of the database file (default is "db_sqlite")
    :return: A list of prices from the 'users' table
    """
    with connect(f"{db_name}.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT price FROM users;")
        prices = cursor.fetchall()
        return [price[0] for price in prices] if prices else []


def data_knapsack_solver(prices: list[float], budget: int) -> tuple[int, list[int], int]:
    """ Get the maximum number of items that can be purchased within the budget.
    :param prices: List of item prices
    :param budget: Total budget available for purchasing items
    :return: A tuple containing the maximum number of items that can be purchased and the list of indices of the selected items
    """
    # Transform the prices to integers if they are not already
    prices: list[int] = [int(price) for price in prices]
    # The number of items (prices)
    n: int = len(prices)

    # Set a dynamic programming array to store the maximum number of items that can be purchased with a given budget
    dp = [0] * (budget + 1)
    # Record the path of selected items
    paths: list[int] = [-1] * (budget + 1)

    # To avoid selecting the same item multiple times, we use a path array to track the last selected item for each budget
    for i in range(n):
        price: int = prices[i]
        for b in range(budget, price - 1, -1):
            if dp[b] < dp[b - price] + 1:
                dp[b] = dp[b - price] + 1
                paths[b] = i

    # # Set the path to backtrack the selected items
    selected_indices: list[int] = []
    # Set to track used items to avoid duplicates
    used_items: set[int] = set()
    # Start from the budget and backtrack to find the selected items
    b = budget
    # Initialise the cost of the selected items
    cost: int = 0

    while b >= 0 and paths[b] != -1:
        i = paths[b]
        if i in used_items:
            b -= 1
            # If the item has already been used, skip it.
            continue
        selected_indices.append(i)
        used_items.add(i)
        b -= prices[i]
        cost += prices[i]

    # Calculate the remaining budget after purchasing the selected items
    balance: int = budget - cost

    return len(selected_indices), selected_indices[::-1], balance


def selected_data_filter(statement: str, selected_indices: list[int], db_name: str = "db_sqlite") -> DataFrame:
    """ Filter the selected data based on the provided indices.
    :param statement: The SQL statement to filter
    :param selected_indices: The indices of the selected items
    :param db_name: The name of the database file (default is "db_sqlite")
    :return: A filtered DataFrame
    """
    # Check if the selected indices are duplicated
    print("Selected indices:", selected_indices)
    print("Unique indices:", list(set(selected_indices)))
    print("Are there duplicates?", len(selected_indices) != len(set(selected_indices)))

    with connect(f"{db_name}.db") as connection:
        # Get a dataframe
        df = read_sql_query(statement, connection)

    return df.iloc[selected_indices]


def flat_data_display(selected_df: DataFrame) -> DataFrame:
    """ Flatten the selected data and return a DataFrame for display.
    :param selected_df: The DataFrame to flatten
    :return: A flattened DataFrame
    """
    rows: list = []
    for _, row in selected_df.iterrows():
        content = loads(str(row["content"]))
        others: dict = row.drop("content").to_dict()
        for item in content:
            row = {**others, **item}
            rows.append(row)

    return json_normalize(rows)
