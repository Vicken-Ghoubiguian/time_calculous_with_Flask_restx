#
from flask import Flask
from flask_restx import Resource, Api

#
time_calculous_function = ['number_of_days_in_choosen_month_in_choosen_year', 'wished_number_in_year_is_day_in_choosen_year', 'wished_wday_in_choosen_year']

#
time_calculous_with_flask_restx = Flask(__name__)
time_calculous_api = Api(time_calculous_with_flask_restx, title='time_calculous API', description='Coming !')

#
ns_time_calculous = time_calculous_api.namespace('time_calculous_operations', description='time_calculous operations for')

#
@ns_time_calculous.route('/introduction')
class Time_calculous_presentation_route(Resource):
    def get(self):

        """
        Route 1, coming !
        """

        return {'presentation' : '', 'description': '', 'github' : 'https://github.com/Vicken-Ghoubiguian/time_calculous_with_Flask_restx', 'dockerhub' : '', 'time_calculous' : 
'https://github.com/Vicken-Ghoubiguian/time_calculous'}, 200

#
@ns_time_calculous.route('/documentation/<string:function>', doc={'params': {'function': 'Choosed function of the "time_calculous" C library to execute'}})
@ns_time_calculous.param('function', 'function', _in='query', type=str, enum=time_calculous_function)
class Time_calculous_main_route(Resource):
    def get(self,function):

        """
        Route 2, coming !
        """

        return {'function': function}, 200

#
if __name__ == '__main__':

    #
    time_calculous_with_flask_restx.run(debug=True)
