from pymongo import MongoClient


client = MongoClient('xxx',1234)
db = client['xxx']
db.authenticate('xxx','xxxx')

# interface for gold data layer to update DB

def add_course_title(course_title, quarter, subject):
    '''

    :param title: title of course as a string
    :param quarter:
    :param subject:
    :return:
    '''
    courses = db.course_titles

    select_quarter = courses.find_one({"quarter":quarter})

    if not select_quarter:
        courses.insert_one({"quarter": quarter})

        courses.update_one({"quarter": quarter},{"$addToSet": {subject: course_title}})

    else:
        courses.update_one({"quarter" : quarter}, {"$addToSet": {subject: course_title}})


def bulk_add_course_titles(titles, quarter, subject):
    '''

    :param titles: array filled with course titles
    :param quarter:
    :param subject:
    :return:
    '''
    for course_title in titles:
        add_course_title(course_title, quarter, subject)


def add_all_offering_info(course_title ,data, quarter, subject):
    courses = db.courses
    course_title = course_title.replace(".","")
    data = { "course title" : course_title, "offerings" : data}

    select_quarter = courses.find_one({"quarter": quarter})

    if not select_quarter:
        courses.insert_one({"quarter":quarter})

        courses.update_one({ "quarter" : quarter}, {"$addToSet": { subject : {course_title: data}}})

    else:

        courses.update_one({"quarter": quarter}, {"$addToSet": {subject: {course_title: data}}})




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

