#!/usr/bin/env python
"""
Description: class for converting comma separated values to JSON format
"""
"""
@author : CupakabraNo1
@contact : vldnovak555@gmail.com
@date : 05.12.2020
@version : 1.0
"""
from os.path import dirname, abspath
import os
import csv
import json
import app.variables as var

class DataConverter():

    def __init__(self) -> None:
        super().__init__()
        self.root_directory = dirname(dirname(abspath(__file__)))

    # @staticmethod
    def convert(self, file_name):
        data = []
        with open(self.root_directory+var.STORAGE_ROOT+"csv/"+file_name+var.CSV_EXTENTION, "r", encoding='latin-1') as csvFile:
            csvReader = csv.DictReader(csvFile)
            counter = 0
            for rows in csvReader:
                if counter < var.MAX_ENTRY_NUMBER:
                    del rows["Id"]
                    data.append(rows)
                    counter+=1
                else:
                    pass
        return data