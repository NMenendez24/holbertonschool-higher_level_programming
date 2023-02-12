#!/usr/bin/python3


"""adds all arguments to a Python list, and then save them to a file"""


save_to_json_file = __import__('5-save_to_json').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
from sys import argv



obj_list = []
for i in range(1, len (argv)):
    obj_list.append(argv[i])
save_to_json_file(obj_list, 'add_item.json')
