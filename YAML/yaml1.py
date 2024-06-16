#!/usr/bin/python3

import yaml


try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

if __name__ == '__main__':
    with open("test1.yaml", 'r') as stream:
        try:
            dictionary = yaml.load(stream, Loader=yaml.SafeLoader)
            for key, value in dictionary.items():
                print (f"{key} : {value}")
        except yaml.YAMLError as exc:
            print(exc)
