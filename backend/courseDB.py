from pymongo import MongoClient


client = MongoClient('xxx',1234)
db = client['xxx']
db.authenticate('xxx','xxx')

# TODO: re-organize data in the db, dont put it all in one.
# TODO: Parse data in better form to give to client in get_course_offerings()

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

def get_course_titles(quarter, subject):
    database = db.course_titles
    try:
        return database.find_one({"quarter": quarter})[subject]
    except (TypeError, KeyError):
        return []



def get_course_offerings(quarter, subject, course_title):
    # returns every course offering for a given course, including section data
    course_title = " " + course_title
    database = db.courses
    given_quarter = database.find({"quarter": quarter})
    results = given_quarter.distinct(subject)
    data = []
    i = 0
    while not data and i != len(results):
        data = results[i].get(course_title)
        i += 1
    return data







