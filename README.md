[![Build Status](https://travis-ci.org/leumas95/j2cli_3.svg)](https://travis-ci.org/leumas95/j2cli_3)

j2cli_3 - Jinja2 Command-Line Tool
================================

`j2cli_3` is a command-line tool for templating in shell-scripts, 
leveraging the [Jinja2](http://jinja.pocoo.org/docs/) library.

Features:

* Jinja2 templating
* Allows to use environment variables! Hello [Docker](http://www.docker.com/) :)
* INI, YAML, JSON data sources supported

Based on [kolypto/j2cli](https://github.com/kolypto/j2cli)

## Installation

```
pip3 install j2cli_3
```

To enable the YAML support with [pyyaml](http://pyyaml.org/):

```
pip3 install j2cli_3[yaml]
```

## Usage

Compile a template using INI-file data source:

    $ j2 config.j2 data.ini
    
Compile using JSON data source:

    $ j2 config.j2 data.json
    
Compile using YAML data source (requires PyYAML):

    $ j2 config.j2 data.yaml

Compile using JSON data on stdin:

    $ curl http://example.com/service.json | j2 --format=json config.j2

Compile using environment variables (hello Docker!):
    
    $ j2 config.j2
    
Or even read environment variables from a file:

    $ j2 --format=env config.j2 data.env
    
# Reference
`j2` accepts the following arguments:

* `template`: Jinja2 template file to render
* `data`: (optional) path to the data used for rendering. The default is `-`: use stdin

Options:

* `--format, -f`: format for the data file. The default is `?`: guess from file extension.

There is some special behavior with environment variables:

* When `data` is not provided (data is `-`), `--format` defaults to `env` and thus reads environment variables
* When `--format=env`, it can read a special "environment variables" file made like this: `env > /tmp/file.env`

## Formats


### env
Data input from environment variables.

Render directly from the current environment variable values:

    $ j2 config.j2

Or alternatively, read the values from a file:

```
NGINX_HOSTNAME=localhost
NGINX_WEBROOT=/var/www/project
NGINX_LOGS=/var/log/nginx/
```

And render with:

    $ j2 config.j2 data.env
    $ env | j2 --format=env config.j2.

This is especially useful with Docker to link containers together.

### ini
INI data input format.

data.ini:

```
[nginx]
hostname=localhost
webroot=/var/www/project
logs=/var/log/nginx/
```

Usage:

    $ j2 config.j2 data.ini
    $ cat data.ini | j2 --format=ini config.j2

### json
JSON data input format

data.json:

```
{
    "nginx":{
        "hostname": "localhost",
        "webroot": "/var/www/project",
        "logs": "/var/log/nginx/"
    }
}
```

Usage:

    $ j2 config.j2 data.json
    $ cat data.json | j2 --format=ini config.j2

### yaml
YAML data input format.

data.yaml:

```
nginx:
  hostname: localhost
  webroot: /var/www/project
  logs: /var/log/nginx
```

Usage:

    $ j2 config.j2 data.yml
    $ cat data.yml | j2 --format=yaml config.j2




Extras
======

## Filters


### `docker_link(value, format='{addr}:{port}')`
Given a Docker Link environment variable value, format it into something else.

This first parses a Docker Link value like this:

    DB_PORT=tcp://172.17.0.5:5432

Into a dict:

```python
{
  'proto': 'tcp',
  'addr': '172.17.0.5',
  'port': '5432'
}
```

And then uses `format` to format it, where the default format is '{addr}:{port}'.

More info here: [Docker Links](https://docs.docker.com/userguide/dockerlinks/)
