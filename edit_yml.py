import sys
import ruamel.yaml


# def edit_yml(input):
#     print(input)

# yaml = ruamel.yaml.YAML()
# # yaml.preserve_quotes = True
# with open('files/web_server.yml') as fp:
#     data = yaml.load(fp)
# for elem in data:
#     if elem['name'] == 'sense2':
#         elem['value'] = 1234
#         break  # no need to iterate further
# yaml.dump(data, sys.stdout)

import yaml
with open('ansible-files/main.yml') as info:
    info_dict = yaml.load(info)

print(info_dict)
