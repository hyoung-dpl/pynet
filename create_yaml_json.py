#!/usr/bin/env python
'''
Write to a yaml and json file for a list and dictionary variable
'''

import yaml
import json

def main():

  yaml_json_dictionary = {
    'code_version':  '11.5',
    'vlan':          '404',
  }

  yaml_json_list = [
    'Location',
    'Manager',
    yaml_json_dictionary,
    'Closet 55'
  ]

  with open(yaml_file, "w") as out
    out.write(yaml.dump(yaml_json_list))

  with open(json_file, "w") as out
    json.dump(yaml_json_list, out)

if __name__ == "__main__":
    main()
