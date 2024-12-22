from flask import Flask
from flask_restx import Resource, Api

time_calculous_with_flask_restx = Flask(__name__)
time_calculous_api = Api(time_calculous_with_flask_restx, title='time_calculous API', description='Coming !')

ns_time_calculous = time_calculous_api.namespace('time_calculous_operations', description='time_calculous operations for')

@ns_time_calculous.route('')
class Time_calculous_presentation_route(Resource):
    def get(self):

        """
        Route 1, coming !
        """

        return {'presentation' : '', 'description': '', 'github' : 'https://github.com/Vicken-Ghoubiguian/time_calculous_with_Flask_restx', 'dockerhub' : '', 'time_calculous' : 
'https://github.com/Vicken-Ghoubiguian/time_calculous'}, 200

@ns_time_calculous.route('/<string:function>/<int:id>/<int:id_1>', doc={'params': {'function': 'Choosed function of the "time_calculous" C library to execute', 'id': 'An ID', 'id_1': 'An ID_1'}})
class Time_calculous_main_route(Resource):
    def get(self,function,id,id_1):

        """
        Route 2, coming !
        """

        return {'function': function, 'nbr': id, 'nbr_1': id_1}, 200

if __name__ == '__main__':
    time_calculous_with_flask_restx.run(debug=True)
