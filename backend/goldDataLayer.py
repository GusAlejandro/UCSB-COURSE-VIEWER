# script that will run every X hours and update the DB with data coming directly from gold
from ucsbGoldApi import goldScraper
from courseDB import *
import collections, time

def update_all_course_titles(quarters, subjects):
    # Can do repeated uploads, doesn't create duplicates
    for quarter in quarters:
        for subject in subjects:
            header = subject + " " + quarter
            response = goldScraper.get_course_titles_for(quarter, subject)
            course_titles = response[header]

            if len(course_titles) != 0: # might move validations to courseDB funcs
                bulk_add_course_titles(course_titles, quarter, subject)


def update_all_data(quarter, subject):
    # CANNOT do repeated uploads, creates duplicates in the db
    # needs the db's to be deleted and rebooted, needs a fresh db
    response = goldScraper.get_all_info_for_courses_in(quarter,subject)
    for key, value in response.items():
        bundle = collections.OrderedDict()
        for id, offering in value.items():
            bundle[id] = [offering]
        print(str(key))
        add_all_offering_info(key ,bundle, quarter, subject)

def bulk_update_all_data(quarters, subjects):
    for quarter in quarters:
        for subject in subjects:
            update_all_data(quarter, subject)


#update_course_titles(qts, subj)
#qts = ["FALL2017","SPRING2017","WINTER2017","FALL2016"]
qts = ["WINTER2017"]
subj = ['ANTH', 'ART', 'ARTHI','ARTST','ASAM','ASTRO','BIO','BMSE','BLST',
    'CHEMENG','CHEMBIO','CHST' ,'CHIN','CLASS' ,'COMM','COMLIT','CMPSC',
    'CMPTG','CNCSP','DANCE','DYNS','EARTH','EACS','EEMB','ECON','EDU',
    'ECE','ENGR','ENGL','ESM','ENVST','ESS','ES','FEMST','FAMST','FRENCH',
    'GENST','GEOG','GER','GPS','GLOBL','GRAD','GREEK','HEB','HIST','INT','ITAL',
    'JAPAN','KOR','LATIN','LATST','LING','LIT','MARSC','MATRL','MATH','MENG',
    'MAT','MST','MEST','MS','MCDB','MUS','MPL','PHIL','PHYS','POLS','PORTU','PSY',
    'RST','RENST','SLAV','SOC','SPAN','SHS','PSTAT','TMP','THTR','WRIT','WL']



"""
this is for updating the full info one 
create new db, populate db by running bulk update
when process is done, redirect all traffic to this new db, delete the old db 
"""

#TODO: create full on update script, with redirection of traffic to update db without any downtime
# start = time.time()
# bulk_update_all_data(qts, subj)
# end = time.time()
# print(str(end-start))
#update_all_course_titles(qts,subj)