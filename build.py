# -*- coding: utf-8 -*-
import hashlib
import json
import os
import sys

from jinja2 import Environment, FileSystemLoader


def get_experiments():
    experiments = []
    for filename in os.listdir('data'):
        experiments.append(json.load(open(os.path.join('data', filename), 'r')))

    return experiments

def build():
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    data = {
        'experiments': get_experiments(),
    }
    output = template.render(data)
    open('index.html', 'w').write(output.encode('utf-8'))


if __name__=='__main__':
    build()
