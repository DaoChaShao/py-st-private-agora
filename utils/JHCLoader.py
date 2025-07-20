#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/19 19:13
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   JHCLoader.py
# @Desc     :   

from streamlit.components.v1 import html


class JHCSetter:
    """ Load HTML, CSS, and JavaScript for embedding in Streamlit. """

    def __init__(self):
        self._mode: str = "r"
        self._encoding: str = "utf-8"

    def set_javascript(self, js_name: str) -> str:
        with open(f"{js_name}.js", self._mode, encoding=self._encoding) as js:
            return f"<script>{js.read()}</script>"

    def set_html(self, html_name: str) -> str:
        with open(f"{html_name}.html", self._mode, encoding=self._encoding) as html:
            return html.read()

    def set_css(self, css_name: str) -> str:
        with open(f"{css_name}.css", self._mode, encoding=self._encoding) as css:
            return f"<style>{css.read()}</style>"


def jhc_loader(js_name: str, html_name: str, css_name: str, height: int = 600, scrolling: bool = True) -> str:
    """ Load JavaScript, CSS, and HTML for embedding in Streamlit.
    :param js_name: Name of the JavaScript file (without extension).
    :param css_name: Name of the CSS file (without extension).
    :param html_name: Name of the HTML file (without extension).
    :param height: Height of the embedded content in pixels.
    :param scrolling: Whether to allow scrolling in the embedded content.
    :return: Combined HTML string with embedded CSS and JavaScript.
    """
    jhc_setter = JHCSetter()
    content = (
            jhc_setter.set_javascript(js_name) +
            jhc_setter.set_html(html_name) +
            jhc_setter.set_css(css_name)
    )
    html(content, height=height, scrolling=scrolling)
