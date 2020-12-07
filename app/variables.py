#!/usr/bin/env python
"""
Description: script containing variables and constant used globaly
"""
"""
@author : CupakabraNo1
@contact : vldnovak555@gmail.com
@date : 05.12.2020
@version : 1.0
"""

from enum import Enum

HOST_KEY = "HOST"
PORT_KEY = "PORT"
USERNAME_KEY = "USERNAME"
PASSWORD_KEY = "PASSWORD"
DATABASE_KEY = "DATABASE"
COLLECTION_KEY = "COLLECTION"

STORAGE_ROOT = "/storage/"
MAX_ENTRY_NUMBER = 1000000

CSV_EXTENTION = ".csv"
JSON_EXTENTION = ".json"

class Table(Enum):
    QUESTIONS = "Questions"
    ANSWERS = "Answers"
    TAGS = "Tags"

connection_parameters = {}
