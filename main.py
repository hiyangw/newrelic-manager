import sys

from lib.utility.utility import logging, check_function, check_api_key, check_api
from lib.utility.functions import functions


def main():
    arguments = sys.argv[1:]
    logging.debug(arguments)
    parameters = {
        'api': arguments[0],
        'function': arguments[1],
        'format': arguments[2],
        'save': (False, True)[arguments[3] == "True"],
        'filters': arguments[4],
        'restore': (False, True)[arguments[5] == "True"]
    }
    logging.debug(parameters)
    api_key = check_api_key()
    api = check_api(parameters['api'])
    check_function(api, parameters['function'])
    functions(api_key, parameters)


if __name__ == "__main__":
    main()
