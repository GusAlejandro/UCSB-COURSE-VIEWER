# layer between the API endpoints and the DB
from pymongo import MongoClient


client = MongoClient('xxx',123456)
db = client['xxx']
db.authenticate('xxx','xxx')


def add_course(name):
    # adds a course to db, including all sections
    # users = db.users
    # users.insert_one({'name':name})

def get_course_offerings(course_title):
    # returns every course offering for a given course, no section data
    pass
def get_all_course_data(course_title):
    # returns every offering for a given course, includes section data
    pass

def get_all_data(quarter, subject):
    # returns all data (offerings and sections) for every course given a quarter and subject
    pass

def get_all_courses(quarter, subject)
    # returns every course (title only) for a given quarter subject
    pass

