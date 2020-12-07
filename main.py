#!/usr/bin/env python
"""
Description: main python script
"""
"""
@author : CupakabraNo1
@contact : vldnovak555@gmail.com
@date : 05.12.2020
@version : 1.0
"""

import app.variables as variables
from app.my_mongo_client import MyMongoClient
from app.data_converter import DataConverter


def main():

    read_parameters()
    my_mongo_client = MyMongoClient()
    
    data_converter = DataConverter()

    for table in variables.Table:
      print(table.value)
      
      items = data_converter.convert(table.value)
      my_mongo_client.populate_database(table.value.lower(), items)


def read_parameters():
    variables.connection_parameters = {}
    f = open("variables.txt", "r")
    lines = f.readlines()
    for line in lines:
        (key, value) = line.split("=")
        variables.connection_parameters[key.strip()] = value.strip()
    print("-------------------------------")
    print("Connection parameters uploaded!")
    print("-------------------------------")


if __name__ == "__main__":
    main()
