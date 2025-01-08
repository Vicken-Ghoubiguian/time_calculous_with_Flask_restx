# Import all necessary Python modules
from flask import Flask
from flask_restx import Resource, Api
from ctypes import *
from os import path, system

#
so_time_calculous_file = "time_calculous.so"

#
if not path.exists(so_time_calculous_file):

    #
    system("git clone https://github.com/Vicken-Ghoubiguian/time_calculous")
    system("cc -fPIC -shared -o time_calculous.so time_calculous/time_calculous/time_calculous.c")

#
time_calculous_functions = CDLL(so_time_calculous_file)

# Definition of the 'time_calculous_function' array which contains all functions in the 'time_calculous' C library
time_calculous_function = ['number_of_days_in_choosen_month_in_choosen_year', 'wished_number_in_year_is_day_in_choosen_year', 'wished_wday_in_choosen_year']

#
time_calculous_with_flask_restx = Flask(__name__)
time_calculous_api = Api(time_calculous_with_flask_restx, title='time_calculous API', description='Coming !')

# Definition of all namespaces
ns_time_calculous_documentation = time_calculous_api.namespace('documentation', description='API routes for complete presentation and documentation of the time_calculous API and the used functions')
ns_time_calculous_functions = time_calculous_api.namespace('functions', description='for test')

#
@ns_time_calculous_documentation.route('/presentation')
class Time_calculous_documentation_presentation_route(Resource):
    def get(self):

        """
        Presentation of the time_calculous API with all useful and resourceful links
        """

        return {'presentation' : '', 'description': '', 'github' : 'https://github.com/Vicken-Ghoubiguian/time_calculous_with_Flask_restx', 'dockerhub' : '', 'time_calculous' : 
'https://github.com/Vicken-Ghoubiguian/time_calculous'}, 200

#
@ns_time_calculous_documentation.route('/lexicon/<string:function>', doc={'params': {'function': 'Choosed function of the "time_calculous" C library to execute'}})
@ns_time_calculous_documentation.param('function', 'function', _in='query', type=str, enum=time_calculous_function)
class Time_calculous_documentation_lexicon(Resource):
    def get(self,function):

        """
        Presentation and description of all available functions in the time_calculous API from the time_calculous C library
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

        #
        result = time_calculous_functions.number_of_days_in_choosen_month_in_choosen_year(month, year)

        return {'year' : year, 'month' : month, 'result' : result}, 200

#
@ns_time_calculous_functions.route('/number_of_weeks_in_a_year_according_to_the_iso_norm/<int:year>', doc={})
@ns_time_calculous_functions.param('year', 'year', _in='query', type=int)
class Time_calculous_functions_numberOfWeeksInAYearAccordingToTheIsoNorm(Resource):
    def get(self, year):

        """
        Route 4, coming !
        """

        #
        result = time_calculous_functions.number_of_weeks_in_a_year_according_to_the_iso_norm(year)

        #
        return {'year' : year, 'result' : result}, 200

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

        #

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

        #
        result = time_calculous_functions.wished_number_in_year_is_day_in_choosen_year(mday, month, year)

        #
        return {'mday' : mday, 'month' : month, 'year' : year, 'result' : result}, 200

#
if __name__ == '__main__':

    #
    time_calculous_with_flask_restx.run(debug=True)
