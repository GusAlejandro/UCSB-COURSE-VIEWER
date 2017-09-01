from pymongo import MongoClient

client = MongoClient('xxx',12345)
db = client['xxx']
db.authenticate('xxx','xxxx')

# functions for DB updates

def add_course_title(course_title, quarter, subject):
    '''

    :param title: title of course as a string
    :param quarter:
    :param subject:
    :return:
    '''
    titles = db.titles

    select_quarter = titles.find_one({"quarter":quarter})

    if not select_quarter:
        # this means that the quarter does not exist, so we need to add it before adding the course
        # create the quarter
        select_quarter = titles.insert_one({"quarter":quarter}).inserted_id
        # now update the quarter with the course
        titles.update({'_id': select_quarter}, {"$addToSet": {subject: course_title}})
    else:
        # this means that the quarter exists so we can just do update since it will create it if not already there
        titles.update({'_id':select_quarter['_id']}, {"$addToSet": {subject : course_title}})










def bulk_add_course_titles(titles, quarter, subject):
    '''

    :param titles: array filled with course titles
    :param quarter:
    :param subject:
    :return:
    '''
    for course_title in titles:
        add_course_title(course_title, quarter, subject)


# interface for clients

def get_course_offerings(course_title):
    # returns every course offering for a given course, no section data
    pass
def get_all_course_data(course_title):
    # returns every offering for a given course, includes section data
    pass

def get_all_data(quarter, subject):
    # returns all data (offerings and sections) for every course given a quarter and subject
    pass

def get_all_courses(quarter, subject):
    # TODO: Implement this with existing data in DB
    # returns every course (title only) for a given quarter subject
    pass

