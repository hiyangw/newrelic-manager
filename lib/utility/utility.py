import json
import os
import yaml
import logging

from ..config import config, schema

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)


def check_api_key():
    key = os.environ['NEW_RELIC_API_KEY']
    if key is None or '':
        logging.error('Please set a correct API Key!')
        exit()
    return key


def check_function(api, function):
    logging.debug('Function: {}'.format(function))
    functions = config.config[api]['functions']
    if function is None or function not in functions:
        logging.error(
            'Please set a correct functions({})!'.format(' | '.join(functions)))
        exit()
    return function


def check_api(api):
    logging.debug('API: {}'.format(api))
    if api is None or api not in config.config:
        logging.error('Please set a correct New relic REST APIs({})!'.format(
            ' | '.join(config.config.keys())))
        exit()
    return api


def check_id(parameters):
    id_sets = parameters['id']
    if id_sets == 'None' or id_sets is None:
        logging.error(
            'No ids in {} parameters, Please use --id to pass ids (ex. --id 123,123)!'.format(parameters['api']))
        exit()
    ids = id_sets.split(',')
    if len(ids) < 1:
        logging.error(
            'Please check your enter ids({}) are correct !'.format(id_sets))
        exit()
    logging.debug('IDs: {}'.format(ids))
    return ids


def parse_filters(api_parameters, parameters):
    api_parameters = api_parameters.copy()
    api_parameters.pop('response_key', None)
    filters = parameters['filters']
    logging.debug(filters)
    function = parameters['function']
    if function == 'create' and filters != 'all':
        logging.error('{} not support filter'.format(function))
        exit()
    if filters == 'all':
        return None
    if '=' in filters:
        filter_items = filters.split('=', 1)
    else:
        logging.error(
            'Incorrect filter format, Please check your filters{}'.format(
                list(item + '={value}' for item in api_parameters)))
        exit()
    filter_key = filter_items[0]
    filter_value = filter_items[1]
    if filter_key in api_parameters:
        filter_name = api_parameters[filter_key]
    else:
        logging.error('Incorrect filter name, {} support filters{}'.format(function, list(
            item + '={value}' for item in api_parameters)))
        exit()
    logging.debug('Filter name: {} | Filter value: {}'.format(
        filter_key, filter_value))
    if filter_key == 'id':
        filter_value = filter_value.split(',')
        filter_value = list(int(value) for value in filter_value)
    filters = {filter_name: filter_value}
    logging.debug(filters)
    return filters


# Parses configure files out of configure/ directory


def load_configure(api, function, file_format):
    configure = None
    if file_format == '':
        logging.error(
            'Please set backup file format(ex: --format=json | yaml)')
        exit()
    if function in ['create', 'update']:
        if file_format == 'json':
            configure = json.load(open('configure/{}.json'.format(api), 'r'))
        if file_format == 'yaml':
            configure = parse_yaml('configure/{}.yaml'.format(api))
    logging.info('Loading {} configuration...'.format(api))
    return configure


def parse_yaml(file):
    try:
        return yaml.load(open(file, 'r'))
    except yaml.YAMLError as exc:
        logging.exception('Error while parsing YAML file:')
        if hasattr(exc, 'problem_mark'):
            if exc.context is not None:
                logging.warning('  parser says\n' + str(exc.problem_mark) + '\n  ' +
                                str(exc.problem) + ' ' + str(exc.context) +
                                '\nPlease correct data and retry.')
            else:
                logging.warning('  parser says\n' + str(exc.problem_mark) + '\n  ' +
                                str(exc.problem) + '\nPlease correct data and retry.')
        else:
            logging.warning('Something went wrong while parsing yaml file')
        return


def valid_configure(api):
    configure = parse_yaml('configure/{}.yaml'.format(api))
    logging.info('Loading {} configuration...'.format(api))
    if len(configure) < 1:
        logging.error(
            '{} configure is empty! Please check your configuration'.format(api))
        exit()
    api_schema = schema.schema[api]
    return configure


def save_file(folder, filename, file_format, data):
    if file_format == 'json':
        data = json.dumps(data, indent=4, sort_keys=True)
    if file_format == 'yaml':
        data = yaml.dump(data, explicit_start=True, default_flow_style=False)
    with open('{}/{}.{}'.format(folder, filename, file_format), 'w') as f:
        f.write(data)
        f.close()
    logging.info('Saved file: {}.{}'.format(filename, file_format))


def json_dump(data):
    return json.dumps(data, indent=4, sort_keys=True)
