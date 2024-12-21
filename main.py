from flask import Flask
from flask_restx import Resource, Api

time_calculous_with_flask_restx = Flask(__name__)
time_calculous_api = Api(time_calculous_with_flask_restx, 
title='time_calculous API', description='Coming !')

@time_calculous_api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    time_calculous_with_flask_restx.run(debug=True)
