#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/20 22:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   trade.py
# @Desc     :   

from streamlit import (sidebar, subheader, empty, number_input, selectbox,
                       caption, slider, markdown)

empty_messages: empty = empty()
# empty_descriptions: empty = empty()

with sidebar:
    subheader("Data Trading Settings")
    # Set your budget
    budget: int = number_input(
        "Set Your Budget",
        min_value=100, max_value=10000, value=1000, step=100,
        help="Set the budget you want to allocate for trading data."
    )
    caption(f"Your budget is set to **${budget}**.")

    # Set the data duration
    duration: int = slider(
        "Select the Duration of Data",
        min_value=7, max_value=28, value=7, step=7,
        help="Choose the duration for which you want to trade data (weekly)."
    )
    caption(f"The duration you selected is **{duration} day(s)**.")

# Set the category of data
categories: list[str] = ["Social Media", "Short Video", "Mobile Payment", "Health & Fitness", "Maps & Navigation"]
category: str = selectbox(
    "Select a Category of the Data",
    ["Select a category"] + categories, index=0,
    help="Choose a category of data to be ready to trade."
)
if category != "Select a category":
    caption(f"The category you selected is **{category}**.")
    empty_messages.info(f"Here you can trade the data related to **{category}**.")

    # Display a description of the selected category
    subheader("**Data Description**")
    match category:
        case "Social Media":
            markdown("- 数据来源于用户在社交媒体平台上的行为。")
            markdown("- 字段包括：观看时长、点赞、评论、分享等互动数据，以及平台偏好、话题兴趣、使用设备与打赏支付方式。")
            markdown("- 适用于用户画像、内容推荐、广告投放等用途。")
        case "Short Video":
            markdown("- 数据来源于用户在短视频平台上的行为。")
            markdown("- 字段包括：视频类型、观看时长、点赞、评论、收藏、分享、单次观看时长、活跃时段、设备、位置、支付方式等。")
            markdown("- 适用于用户画像、内容推荐、广告投放等用途。")
        case "Mobile Payment":
            markdown("- 数据来源于用户在移动支付平台上的交易行为。")
            markdown("- 字段包括：支付设备、支付方式、交易种类、交易总额、交易次数、平均单笔金额、支付高峰时段、支付地点等。")
            markdown("- 适用于金融画像、消费能力分析等用途。")
        case "Health & Fitness":
            markdown("- 数据来源于用户在健康与健身应用上的活动。")
            markdown("- 字段包括：运动时长、消耗卡路里、步数、平均心率、高峰锻炼时间、运动设备、类型、地点等。")
            markdown("- 适用于健康管理、健身计划制定等用途。")
        case "Maps & Navigation":
            markdown("- 数据来源于用户在地图与导航应用上的使用情况。")
            markdown("- 字段包括：出行次数、总距离、导航时间、平均速度、交通方式、出行目的、常去地点、设备等。")
            markdown("- 适用于出行规划、交通分析等用途.")
        case _:
            description = "No description available for this category."

    # Set the action for trading
    if sidebar.button(
            "Trade", type="primary", use_container_width=True,
            help="Click to initiate the trading process for the selected data category."
    ):
        pass
else:
    caption("No category selected.")
    empty_messages.info("Please select a category for trading.")
