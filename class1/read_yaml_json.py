#!/usr/bin/env python
'''
Read yaml and json from files
'''

import yaml
import json

from pprint import pprint

def output(in_list, in_str):
    print '\n\n'
    print '#' * 5
    print '#' * 5 + in_str
    print '#' * 5
    pprint(in_list)

def main():
    yaml_file = 'yaml_write.yml'
    json_file = 'json_write.json'

    with open(yaml_file) as in_file:
        yaml_list = yaml.load(in_file)

    with open(json_file) as in_file:
        json_list = json.load(in_file)

    output(yaml_list, ' YAML')
    output(json_list, ' JSON')
    print '\n'

if __name__ == "__main__":
    main()
