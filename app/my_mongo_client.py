#!/usr/bin/env python
"""
Description: class for communicating with Mongo database
"""
"""
@author : CupakabraNo1
@contact : vldnovak555@gmail.com
@date : 05.12.2020
@version : 1.0
"""

import pymongo as pymongo
import app.variables as var
class MyMongoClient():
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(
            var.connection_parameters[var.HOST_KEY], int(var.connection_parameters[var.PORT_KEY]))
        print("-------------------------------")
        print("Connection created!")

        self.database = self.mongo_client[var.connection_parameters[var.DATABASE_KEY]]
        print("Database created!")
        print("-------------------------------")

        

    def populate_database(self, collection_name, items):
        self.collection = self.database[collection_name]
        print("-------------------------------")
        print("Collection "+collection_name+" created!")
        if len(items) > 0:
            x = self.collection.insert_many(items)
            print("Inserted!")
            print("Count:")
            print(len(x.inserted_ids))
            print("-------------------------------")
        else:
            print("Empty list!")
            print("-------------------------------")

    def __del__(self):
      self.mongo_client.close()
      self.database = None
