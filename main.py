# Import all necessary Python modules
from flask import Flask
from flask_restx import Resource, Api

# Definition of the 'time_calculous_function' array which contains all functions in the 'time_calculous' C library
time_calculous_function = ['number_of_days_in_choosen_month_in_choosen_year', 'wished_number_in_year_is_day_in_choosen_year', 'wished_wday_in_choosen_year']

#
time_calculous_with_flask_restx = Flask(__name__)
time_calculous_api = Api(time_calculous_with_flask_restx, title='time_calculous API', description='Coming !')

# Definition of all namespaces
ns_time_calculous_documentation = time_calculous_api.namespace('documentation', description='for test')
ns_time_calculous_functions = time_calculous_api.namespace('functions', description='for test')

#
@ns_time_calculous_documentation.route('/presentation')
class Time_calculous_documentation_presentation_route(Resource):
    def get(self):

        """
        Route 1, coming !
        """

        return {'presentation' : '', 'description': '', 'github' : 'https://github.com/Vicken-Ghoubiguian/time_calculous_with_Flask_restx', 'dockerhub' : '', 'time_calculous' : 
'https://github.com/Vicken-Ghoubiguian/time_calculous'}, 200

#
@ns_time_calculous_documentation.route('/lexicon/<string:function>', doc={'params': {'function': 'Choosed function of the "time_calculous" C library to execute'}})
@ns_time_calculous_documentation.param('function', 'function', _in='query', type=str, enum=time_calculous_function)
class Time_calculous_documentation_lexicon(Resource):
    def get(self,function):

        """
        Route 2, coming !
        """

        return {'function': function}, 200

#
@ns_time_calculous_functions.route('/number_of_days_in_choosen_month_in_choosen_year/<int:month>/<int:year>', doc={})
@ns_time_calculous_functions.param('month', 'month', _in='query', type=int)
@ns_time_calculous_functions.param('year', 'year', _in='query', type=int)
class Time_calculous_functions_numberOfDaysInChoosenMonthInChoosenYear(Resource):
    def get(self, month, year):

        """
        Route 3, coming !
        """

        return {'coming' : 0}, 200

#
@ns_time_calculous_functions.route('/number_of_weeks_in_a_year_according_to_the_iso_norm/<int:year>', doc={})
@ns_time_calculous_functions.param('year', 'year', _in='query', type=int)
class Time_calculous_functions_numberOfWeeksInAYearAccordingToTheIsoNorm(Resource):
    def get(self, year):

        """
        Route 4, coming !
        """

        return {'coming' : 0}, 200

#
@ns_time_calculous_functions.route('/wished_wday_in_choosen_year/<int:number_of_weekday_in_the_year>/<int:month>/<int:year>', doc={})
@ns_time_calculous_functions.param('number_of_weekday_in_the_year', 'number_of_weekday_in_the_year', _in='query', type=int)
@ns_time_calculous_functions.param('month', 'month', _in='query', type=int)
@ns_time_calculous_functions.param('year', 'year', _in='query', type=int)
class Time_calculous_functions_wishedWdayInChoosenYear(Resource):
    def get(self, number_of_weekday_in_the_year, month, year):

        """
        Route 5, coming !
        """

        return {'coming' : 0}, 200

#
@ns_time_calculous_functions.route('/wished_number_in_year_is_day_in_choosen_year/<int:mday>/<int:month>/<int:year>', doc={})
@ns_time_calculous_functions.param('mday', 'mday', _in='query', type=int)
@ns_time_calculous_functions.param('month', 'month', _in='query', type=int)
@ns_time_calculous_functions.param('year', 'year', _in='query', type=int)
class Time_calculous_functions_wishedNumberInYearIsDayInChoosenYear(Resource):
    def get(self, mday, month, year):

        """
        Route 6, coming !
        """

        return {'coming' : 0}, 200

#
if __name__ == '__main__':

    #
    time_calculous_with_flask_restx.run(debug=True)
