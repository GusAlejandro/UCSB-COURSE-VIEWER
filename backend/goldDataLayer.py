# script that will run every X hours and update the DB with data coming directly from gold
from ucsbGoldApi import goldScraper
from ucsbGoldApi.settings import codes_for_quarters, codes_for_subject
from courseDB import *

def update_course_titles(quarters, subjects):
    for quarter in quarters:
        for subject in subjects:
            header = subject + " " + quarter
            response = goldScraper.get_course_titles_for(quarter, subject)
            course_titles = response[header]
            if len(course_titles) != 0: # might move validations to courseDB funcs
                bulk_add_course_titles(course_titles, quarter, subject)



qts = ["SPRING2017","WINTER2017","FALL2016"]
subj = ["MATH","PHYS","CMPSC","MENG"]


update_course_titles(qts, subj)











