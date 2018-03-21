#! /usr/bin/env python

import json
import inspect
from exdoc import doc, getmembers

import j2cli
import j2cli.context
import j2cli.extras.filters


README = {
    'formats': {
        name: doc(f)
        for name, f in list(j2cli.context.FORMATS.items())
    },
    'extras': {
        'filters': [doc(v)
                    for k, v in getmembers(j2cli.extras.filters)
                    if inspect.isfunction(v)]
    }
}

print(json.dumps(README))
