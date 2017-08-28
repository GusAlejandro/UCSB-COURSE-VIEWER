from flask import Flask
from flask_restful import Resource, Api, reqparse
from courseDB import add_course

app = Flask(__name__)
api = Api(app)


class Courses(Resource):
    # def post(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('name', required=True, help="Can't be blank")
    #     args = parser.parse_args()
    #     add(args['name'])
    #     return "added " + args['name'] + " as a user!"

    def post(self):
        pass

    def get(self):
        pass

api.add_resource(Courses, '/api/v1/Courses')


if __name__ == '__main__':
    app.run(debug=True)
