#!/usr/bin/env python
from setuptools import setup
import os

setup(
    name = "ocr_chain",
    version = "0.0.1",
    author = "Daniel Altenburg",
    author_email = "julien.altenburg@gmail.com",
    description = (""),
    long_description=""" """,
    license = "GNU GPL 3",
    keywords = "ocr_chain",
    url = "",
    packages=[
        'ocr_chain',
        'ocr_chain.core'
    ],
    install_requires=[
        'pillow',
        'pytesseract',
    ],
    scripts = [os.path.join('bin','ocr-chain')]
)
