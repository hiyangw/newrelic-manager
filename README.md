# <p align="center">New Relic Manager</p>

## Summary (v1.0.0)
###### This repository provides a tool to manage New Relic resources via [newrelic-api](https://new-relic-api.readthedocs.io) python lib

## Currently Supported Resources

| Resource      |  List              |  Show              |  Update            |  Delete            |  Create            |  Backup            |  Restore       |
|:------------- |:------------------:|:------------------:|:------------------:|:------------------:|:------------------:|:------------------:|:--------------:|
| Users         | :white_check_mark: | :white_check_mark: |   :x:              |   :x:              |    :x:             |   :x:              |   :x:          |
| Applications  | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |    :x:             | :white_check_mark: | :white_circle: |
| Dashboards    | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_circle: |
| Alerts Policies | :white_check_mark: | :x:              | :white_check_mark: | :white_check_mark: | :white_check_mark: | :x:                | :x:            |
| Alerts Channels | :white_check_mark: | :x:              | :x:                | :white_check_mark: | :white_check_mark: | :x:                | :x:            |
| Alerts NRQL Conditions | :white_circle: | :x:           | :white_circle:     |:white_circle:      | :white_circle:     | :white_circle:     | :white_circle: |

:white_check_mark: Supported

:white_circle: Todo

:x: Not support 

## How To Use
| Arguments     | Default | Description |
|:------------- |:-------:|:------------|
| `-h` or `--help` | N/A | Help information |
| `-k` or `--key`  | N/A | New Relic API Key |
| `-s` or `--save` | False | Save output to local |
| `-i` or `--api`  | N/A | Choice an Rest API (applications, dashboards, users etc.) |
| `-f` or `--function` | N/A | Choice an function (list, show, backup etc.) |
| `--format`       | yaml | Support *Json* and *Yaml* default is Json |
| `--filter`       | all | Apply filter (ex: --filter title="SRE") |
| `-r` or `--restore` | N/A | Give a backup file path to restore |

```
./run.sh -k {new relic api key} -f {function} --api {api name} --format {json|yaml} --filter {filter name}={filter value}
```
Examples:

```
./run.sh -k XXXXXXXXX -f show --api dashboards --format json --filter id="123" 
```

## Developing Locally

### Prerequisites
* Python 3
