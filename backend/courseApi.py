from flask import Flask
from flask_restful import Resource, Api, reqparse
from courseDB import get_course_offerings, get_course_titles

app = Flask(__name__)
api = Api(app)


class CourseTitles(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('quarter', required=True)
        parser.add_argument('subject', required=True)
        args = parser.parse_args()
        return get_course_titles(args['quarter'], args['subject'])

api.add_resource(CourseTitles, '/api/v1/CourseTitles')


class Course(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('quarter', required=True)
        parser.add_argument('subject', required=True)
        parser.add_argument('courseTitle', required=True)
        args = parser.parse_args()
        return get_course_offerings(args['quarter'], args['subject'], args['courseTitle'])

api.add_resource(Course, '/api/v1/CourseData')


if __name__ == '__main__':
    app.run(debug=True)
