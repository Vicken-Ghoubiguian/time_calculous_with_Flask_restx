# Import all necessary Python modules
from flask import Flask
from flask_restx import Resource, Api
from ctypes import *
from os import path, system
from enum import Enum

#
class numeral(Enum):
    FIRST = 0
    SECOND= 1
    THIRD = 2
    BEFORE_LAST = 3
    LAST = 4

#
class weekDay(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

#
def configurationTimeCalculous():

    #
    the_GitHub_repos_time_calculous = "https://github.com/Vicken-Ghoubiguian/time_calculous"
    so_time_calculous_file = "time_calculous.so"

    #
    if not path.exists(so_time_calculous_file):

        #
        system("git clone " + the_GitHub_repos_time_calculous)
        system("cc -fPIC -shared -o " + so_time_calculous_file + " time_calculous/time_calculous/time_calculous.c")

    #
    return CDLL(so_time_calculous_file)

#
time_calculous_functions = configurationTimeCalculous()

# Definition of the 'time_calculous_function' array which contains all functions in the 'time_calculous' C library
time_calculous_function = ['number_of_days_in_choosen_month_in_choosen_year', 'wished_number_in_year_is_day_in_choosen_year', 'wished_wday_in_choosen_year']

#
time_calculous_with_flask_restx = Flask(__name__)
time_calculous_api = Api(time_calculous_with_flask_restx, title='time_calculous API', description='Coming !')

# Definition of all namespaces
ns_time_calculous_documentation = time_calculous_api.namespace('documentation', description='API routes for complete presentation and documentation of the time_calculous API and the used functions')
ns_time_calculous_functions = time_calculous_api.namespace('functions', description='API routes for calculations on datetimes using the C library \'time_calculous\'')

#
@ns_time_calculous_documentation.route('/presentation')
class Time_calculous_documentation_presentation_route(Resource):
    def get(self):

        """
        Presentation of the time_calculous API with all useful and resourceful links
        """

        #
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

        #
        return {'function': function}, 200

#
@ns_time_calculous_functions.route('/number_of_days_in_choosen_month_in_choosen_year/<int:month>/<int:year>', doc={})
@ns_time_calculous_functions.param('month', 'month', _in='query', type=int)
@ns_time_calculous_functions.param('year', 'year', _in='query', type=int)
class Time_calculous_functions_numberOfDaysInChoosenMonthInChoosenYear(Resource):
    def get(self, month, year):

        """
        Calculation of the total count of days in the choosen month in the choosen year (the whole datetime according the UTC/GMT timezone)
        """

        #
        result = time_calculous_functions.number_of_days_in_choosen_month_in_choosen_year(month, year)

        #
        return {'year' : year, 'month' : month, 'result' : result}, 200

#
@ns_time_calculous_functions.route('/number_of_weeks_in_a_year_according_to_the_iso_norm/<int:year>', doc={})
@ns_time_calculous_functions.param('year', 'year', _in='query', type=int)
class Time_calculous_functions_numberOfWeeksInAYearAccordingToTheIsoNorm(Resource):
    def get(self, year):

        """
        Calculation of the total count of weeks in the choosing year (the whole datetime according the UTC/GMT timezone)
        """

        #
        result = time_calculous_functions.number_of_weeks_in_a_year_according_to_the_iso_norm(year)

        #
        return {'year' : year, 'result' : result}, 200

#
@ns_time_calculous_functions.route('/wished_wday_in_choosen_year/<int:year>/<int:wday>/<int:number_of_weekday_in_the_year>', doc={'params': {'year': '', 'wday': '', 'number_of_weekday_in_the_year': ''}})
@ns_time_calculous_functions.param('year', 'Wished year', _in='query', type=int)
@ns_time_calculous_functions.param('wday', 'Wished weekday (0 = sunday, 1 = monday, 2 = tuesday, 3 = wednesday, 4 = thursday, 5 = friday, 6 = saturday)', _in='query', type=weekDay, enum=[0, 1, 2, 3, 4, 5, 6])
@ns_time_calculous_functions.param('number_of_weekday_in_the_year', 'Wished number of the chosen weekday in the chosen year', _in='query', type=int)
class Time_calculous_functions_wishedWdayInChoosenYear(Resource):
    def get(self, year, wday, number_of_weekday_in_the_year):

        """
        Calculation of the day according the number of the wished weekday in the wished year (the whole datetime according the UTC/GMT timezone)
        """

        #
        result = time_calculous_functions.wished_wday_in_choosen_year(year, wday, number_of_weekday_in_the_year)

        #
        return {'year' : year, 'wday' : wday, 'number_of_weekday_in_the_year' : number_of_weekday_in_the_year, 'result' : result}, 200

#
@ns_time_calculous_functions.route('/wished_number_in_year_is_day_in_choosen_year/<int:mday>/<int:month>/<int:year>', doc={'params': {'mday': '', 'month': '', 'year': ''}})
@ns_time_calculous_functions.param('mday', 'mday', _in='query', type=int)
@ns_time_calculous_functions.param('month', 'month', _in='query', type=int)
@ns_time_calculous_functions.param('year', 'year', _in='query', type=int)
class Time_calculous_functions_wishedNumberInYearIsDayInChoosenYear(Resource):
    def get(self, mday, month, year):

        """
        Calculation of the number of the choosen mday in the choosen month in the choosen year (the whole datetime according the UTC/GMT timezone)
        """

        #
        result = time_calculous_functions.wished_number_in_year_is_day_in_choosen_year(mday, month, year)

        #
        return {'mday' : mday, 'month' : month, 'year' : year, 'result' : result}, 200
    
#
@ns_time_calculous_functions.route('/wished_wday_in_choosen_month/<int:year>/<int:month>/<int:wday>/<int:hour>/<int:minute>/<int:second>/<int:numeral>', doc={})
@ns_time_calculous_functions.param('year', 'year', _in='query', type=int)
@ns_time_calculous_functions.param('month', 'month', _in='query', type=int)
@ns_time_calculous_functions.param('wday', 'wday', _in='query', type=weekDay, enum=[0, 1, 2, 3, 4, 5, 6])
@ns_time_calculous_functions.param('hour', 'hour', _in='query', type=int)
@ns_time_calculous_functions.param('minute', 'minute', _in='query', type=int)
@ns_time_calculous_functions.param('second', 'second', _in='query', type=int)
@ns_time_calculous_functions.param('numeral', 'numeral', _in='query', type=numeral, enum=[0, 1, 2, 3, 4])
class Time_calculous_functions_wishedWdayInChoosenMonth(Resource):
    def get(self, year, month, wday, hour, minute, second, numeral):

        """
        Calculation of the wished weekday in a choosen month in a choosen year at a choosen time with second, minute, and hour (the whole datetime according the UTC/GMT timezone)
        """

        #
        result = time_calculous_functions.wished_wday_in_choosen_month(year, month, wday, hour, minute, second, numeral)

        #
        return {'year' : year, 'month' : month, 'wday' : wday, 'hour' : hour, 'minute' : minute, 'second' : second, 'numeral' : numeral, 'result' : result}, 200

#
if __name__ == '__main__':

    #
    time_calculous_with_flask_restx.run(debug=True)
