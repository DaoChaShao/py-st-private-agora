#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 14:44
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :   

from utils.layout import window_setter, subpages_setter


def main() -> None:
    """ streamlit run main.py """
    # Set the window configuration
    window_setter()

    # Set the subpages on the sidebar
    subpages_setter()


if __name__ == "__main__":
    main()
