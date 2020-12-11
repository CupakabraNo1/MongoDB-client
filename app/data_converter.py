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




from progress.bar import FillingCirclesBar
import time
import csv
import sys
import datetime
import app.variables as var
from ast import literal_eval
from os.path import dirname, abspath
class DataConverter():

    def __init__(self) -> None:
        super().__init__()
        self.root_directory = dirname(dirname(abspath(__file__)))
        self.bar = None

    def generateDocument(self, rows):
        # class Talk
        doc = {
            #param: int
            "talk_id": int(rows["talk_id"]),
            #param: string
            "talk_name": None if rows["talk_name"] in var.NONE_VALUES else rows["talk_name"],
            #param: int
            "view_count": None if rows["view_count"] in var.NONE_VALUES else int(rows["view_count"]),
            #param: int
            "comment_count": None if rows["comment_count"] in var.NONE_VALUES else int(rows["comment_count"]),
            #param: int
            "duration": None if rows["duration"] in var.NONE_VALUES else int(rows["duration"]),
            #param: string
            "transcript": None if rows["transcript"] in var.NONE_VALUES else rows["transcript"],
            #param: string
            "video_type_name": None if rows["video_type_name"] in var.NONE_VALUES else rows["video_type_name"],
            #param: string
            "event": None if rows["event"] in var.NONE_VALUES else rows["event"],
            #param: int
            "number_of_speakers": None if rows["number_of_speakers"] in var.NONE_VALUES else int(rows["number_of_speakers"]),
            # param: class Speaker
            "speaker":
            # class Speaker
            {
                #param: int
                "id": None if rows["speaker_id"] in var.NONE_VALUES else int(rows["speaker_id"]),
                #param: string
                "name": None if rows["speaker_name"] in var.NONE_VALUES else rows["speaker_name"],
                #param: string
                "description": None if rows["speaker_description"] in var.NONE_VALUES else rows["speaker_description"],
                #param: boolean
                "is_published": False if rows["speaker_is_published"] in var.NONE_VALUES or int(rows["speaker_is_published"]) == 0 else True
            },
            #param: boolean
            "is_featured": bool(rows["speaker_is_published"]),
            #param: date
            "recording_date": None if rows["recording_date"] in var.NONE_VALUES else datetime.datetime.strptime(rows["recording_date"], "%Y-%m-%d"),
            #param: date
            "published_timestamp": None if rows["published_timestamp"] in var.NONE_VALUES else datetime.datetime.strptime(rows["published_timestamp"], "%Y-%m-%d %H:%M:%S"),
            # param: list<string>
            "talks_tags": literal_eval(rows["talks_tags"]),
            #param: int
            "number_of_tags": None if rows["number_of_tags"] in var.NONE_VALUES else int(rows["number_of_tags"]),
            # param: class Language
            "languages":
            # class Language
            {
                #param: string
                "language": None if rows["language"] in var.NONE_VALUES else rows["language"],
                #param: string
                "native": None if rows["native_language"] in var.NONE_VALUES else rows["native_language"],
                #param: boolean
                "swap": bool(rows["language_swap"]),
                #param: boolean
                "language_swap": bool(rows["language_swap"]),
                #param: boolean
                "subtitle_required": bool(rows["is_subtitle_required"]),
            },
            # param: class Url
            "url":
            # class Url
            {
                #param: string
                "webpage": None if rows["url_webpage"] in var.NONE_VALUES else rows["url_webpage"],
                #param: string
                "audio": None if rows["url_audio"] in var.NONE_VALUES else rows["url_audio"],
                #param: string
                "video": None if rows["url_video"] in var.NONE_VALUES else rows["url_video"],
                # param: class Photo
                "photo":
                # class Photo
                {
                    #param: string
                    "talk": None if rows["url_photo_talk"] in var.NONE_VALUES else rows["url_photo_talk"],
                    #param: string
                    "speaker": None if rows["url_photo_speaker"] in var.NONE_VALUES else rows["url_photo_speaker"]
                }
            },
            #param: string
            "talk_recommendations_blurb":  None if rows["talk_recommendations_blurb"] in var.NONE_VALUES else rows["talk_recommendations_blurb"],
            # param: class Duration
            "duration":
            # class Duration
            {
                #param: flat
                "intro": None if rows["intro_duration"] in var.NONE_VALUES else float(rows["intro_duration"]),
                #param: flat
                "ad": None if rows["ad_duration"] in var.NONE_VALUES else float(rows["ad_duration"]),
                #param: flat
                "post_ad": None if rows["post_ad_duration"] in var.NONE_VALUES else float(rows["post_ad_duration"]),
                #param: flat
                "external": None if rows["external_duration"] in var.NONE_VALUES else float(rows["external_duration"]),
            }
        }
        return doc

    def convert(self, file_name):
        data = []
        with open(self.root_directory+var.STORAGE_ROOT+"csv/"+file_name+var.CSV_EXTENTION, "r") as csvFile :
            csv_reader = csv.DictReader(csvFile)
            self.bar = FillingCirclesBar(
                "Reading csv...", max=var.MAX_ENTRY_NUMBER)
            counter = 0
            for rows in csv_reader:
                if counter < var.MAX_ENTRY_NUMBER:
                    document = self.generateDocument(rows)
                    data.append(document)
                    self.bar.next()
                    counter+=1
                else:
                    self.bar.next()
                    pass
            while counter < var.MAX_ENTRY_NUMBER:
                counter += 1
                self.bar.next()
            self.bar.finish()
        return data

