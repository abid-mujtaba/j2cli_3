#! /usr/bin/env python

import json
import inspect
from exdoc import doc, getmembers

import j2cliPy3
import j2cliPy3.context
import j2cliPy3.extras.filters


README = {
    'formats': {
        name: doc(f)
        for name, f in list(j2cliPy3.context.FORMATS.items())
    },
    'extras': {
        'filters': [doc(v)
                    for k, v in getmembers(j2cliPy3.extras.filters)
                    if inspect.isfunction(v)]
    }
}

print(json.dumps(README))
