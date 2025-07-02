# coding: utf-8
from pathlib import Path

# change DEBUG to False if you want to compile the code to exe
DEBUG = "__compiled__" not in globals()


YEAR = 2024
AUTHOR = "HITwhFaceGroup"
VERSION = "Beta 1.0"
APP_NAME = "ExaminationSecuritySystem"
HELP_URL = "https://www.baidu.com"
REPO_URL = "https://www.baidu.com"
FEEDBACK_URL = "https://www.baidu.com"
DOC_URL = "https://www.baidu.com"

CONFIG_FOLDER = Path('AppData').absolute()
CONFIG_FILE = CONFIG_FOLDER / "config.json"
