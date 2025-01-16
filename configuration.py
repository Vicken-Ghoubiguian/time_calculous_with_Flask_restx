from ctypes import *
from os import path, system

#
def configurationTimeCalculous():

    #
    the_GitHub_repos_time_calculous = "https://github.com/Vicken-Ghoubiguian/time_calculous"
    repos_time_calculous = "time_calculous"
    so_time_calculous_file = "time_calculous.so"

    #
    if not path.exists(so_time_calculous_file):

        #
        try:

            #
            system("git clone " + the_GitHub_repos_time_calculous)
        
        #
        except Exception as exception:

            #
            pass

        #
        if not path.isdir(repos_time_calculous) :

            #
            print("\nError : the C library time_calculous' is not available ! Quitting the app !\n")
        
            #
            quit()

        #
        system("cc -fPIC -shared -o " + so_time_calculous_file + " time_calculous/time_calculous/time_calculous.c")

    #
    return CDLL(so_time_calculous_file)