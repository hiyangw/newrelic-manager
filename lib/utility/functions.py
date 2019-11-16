import datetime
import json
import sys

from ..config import config
from ..utility.utility import save_file, logging, parse_filters, valid_configure, json_dump
from newrelic_api import *


def functions(api_key, parameters):
    api = parameters['api']
    function = parameters['function']
    api_parameters = config.config[api]['functions'][function]
    filters = parse_filters(api_parameters, parameters)
    rest_api = getattr(sys.modules[__name__], "%s" %
                       config.config[api]["class_name"])(api_key=api_key)
    getattr(sys.modules[__name__], "f_%s" %
            function)(rest_api, parameters, filters)


def f_list(rest_api, parameters, filters):
    api = parameters['api']
    function = parameters['function']
    response_key = config.config[api]['functions']['list']['response_key']
    fields = config.config[api]['fields']
    items = []
    page = 0
    while True:
        page += 1
        if filters is None:
            response = rest_api.list(page=page)
        else:
            response = rest_api.list(**filters, page=page)
        for item in response[response_key]:
            items.append(item)
        if 'pages' not in response:
            break
        elif 'next' not in response.get('pages'):
            break
    print('------ Found {} {} ------'.format(len(items), api))
    print('------ {} {} ------\n- {}: {}'.format(function,
                                                 api, fields[0], fields[1]))
    markdown = '| {} |\n| :{}\n'.format(' | '.join(
        fields).title().replace('_', ' '), ' ---- |' * len(fields))
    for item in items:
        content = []
        for i in fields:
            string = str(item[i])
            if i.find('url') != -1:
                string = '[link]({})'.format(item[i])
            content.append(string)
        print('- {}: {}'.format(item[fields[0]], item[fields[1]]))
        markdown += '| {} |\n'.format(' | '.join(content))
    print('-----------------------')
    data = {
        api: items
    }
    if parameters['save']:
        file_name = '{}-{}'.format(api, function)
        save_file('output/{}'.format(api), file_name,
                  parameters['format'], data)
    if len(response[response_key]) > 1:
        save_file('output/{}'.format(api), api, 'md', markdown)
    return data


def f_show(rest_api, parameters, filters):
    api = parameters['api']
    function = parameters['function']
    response_key = config.config[api]['functions']['show']['response_key']
    items = []
    for id in filters['id']:
        response = rest_api.show(id)
        items.append(response[response_key])
        print('------ {}: {} ------'.format(function, id))
        if function != 'backup':
            print(json_dump(response))
        if parameters['save']:
            file_name = '{}-{}'.format(api, id)
            save_file('output/{}'.format(api), file_name,
                      parameters['format'], response)
    data = {
        api: items
    }
    return data


def f_create(rest_api, parameters, filters):
    api = parameters['api']
    function = parameters['function']
    response_key = config.config[api]['functions']['create']['response_key']
    configure = valid_configure(api)[api]
    api_parameters = config.config[api]['functions']['create']
    print('------ Create {} ------'.format(api))
    for item in configure:
        name = list(api_parameters.keys())[0]
        key = api_parameters[name]
        f = {
            key: item[name]
        }
        lists = rest_api.list(**f)
        data_name = api_parameters['data']
        if len(lists[api]) < 1:
            json_data = json_dump({response_key: item})
            f_data = {
                data_name: json_data
            }
            print(json_data)
            response = rest_api.create(f_data)
            print(response)
            file_name = '{}-{}-{}'.format(api,
                                          function, response[response_key]['id'])
            save_file('output/{}'.format(api), file_name,
                      parameters['format'], response)
        else:
            logging.error(
                '[{}] already in dashboards, Please check your dashboard title'.format(item[name]))
            print(json_dump(lists))
            continue


def f_update(rest_api, parameters, filters):
    api = parameters['api']
    function = parameters['function']
    response_key = config.config[api]['functions']['update']['response_key']
    configure = valid_configure(api)[api]
    api_parameters = config.config[api]['functions']['update']
    print('------ Update {} ------'.format(api))
    for item in configure:
        id_num = item.get('id')
        if id_num is None:
            logging.error('Please check {} id in configuration'.format(api))
            sys.exit()

        json_data = json_dump({response_key: item})
        data_name = api_parameters['data']
        f_data = {
            data_name: json_data
        }
        print(json_data)
        response = rest_api.create(f_data)
        print(json_dump(response))
        file_name = '{}-{}-{}'.format(api, function,
                                      response[response_key]['id'])
        save_file('output/{}'.format(api), file_name,
                  parameters['format'], response)


def f_delete(rest_api, parameters, filters):
    api = parameters['api']
    function = parameters['function']
    ids = filters["id"]
    for id in ids:
        logging.info('Backup {} to {}'.format(id, api))
        data = rest_api.show(id)
        file_name = '{}-{}'.format(function, id)
        save_file('output/{}'.format(api), file_name,
                  parameters['format'], data)
        response = rest_api.delete(id)
        logging.warning('Deleting {} from {}'.format(id, api))
        print(json_dump(response))
        logging.warning('{}({}) deleted'.format(api, id))


def f_backup(rest_api, parameters, filters):
    api = parameters['api']
    if 'id' in filters:
        response = f_show(rest_api, parameters, filters)
    else:
        items = f_list(rest_api, parameters, filters)[api]
        logging.debug(json_dump(items))
        ids = list(item['id'] for item in items)
        logging.debug(ids)
        response = f_show(rest_api, parameters, {'id': ids})
    ts = datetime.datetime.utcnow().isoformat()
    save_file('output', 'backup-{}-{}'.format(api, ts),
              parameters['format'], response)

# todo


def f_restore(rest_api, parameters, filters):
    api = parameters['api']
