import json

import interactions
import os


def config(path:str):
    with open('./config.json') as config_file:
        config = json.load(config_file)
        return config[path]


