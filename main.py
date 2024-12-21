from flask import Flask
from flask_restx import Resource, Api

time_calculous_with_flask_restx = Flask(__name__)
time_calculous_api = Api(time_calculous_with_flask_restx, 
title='time_calculous API', description='Coming !')

@time_calculous_api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@time_calculous_api.route('/hello_1/<id>/<id_1>', doc={'params': {'id': 'An ID', 'id_1': 'An ID_1'}})
class HelloWorld_1(Resource):
    def get(self,id,id_1):
        return {'nbr': id}

if __name__ == '__main__':
    time_calculous_with_flask_restx.run(debug=True)
