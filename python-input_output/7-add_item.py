#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""

save_to_json_file = __import__('5-save_to_json').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys
import os

def main():
    """Function"""
    if os.path.exists('add_item.json'):
        obj_list = load_from_json_file('add_item.json')
    else:
        obj_list = []
    for i in range(1, len (sys.argv)):
        """Test doc"""
        obj_list.append(sys.argv[i])
    save_to_json_file(obj_list, 'add_item.json')

if __name__ == '__main__':
    main()
