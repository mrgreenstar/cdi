#!/usr/bin/python
import sys
import os

HOME = os.path.expanduser('~')
if __name__ == '__main__':
    available_dir = {}
    try:
        new_dir = os.path.expanduser('~/{}'.format(sys.argv[1]))
    except IndexError:
        print('You should enter the name of directory you want to move to ')
    else:
        # Get the list of all available directories 
        list_dir = os.walk(HOME)
        for i in list_dir:
            for j in i:
                try:
                    result = j.find(sys.argv[1])
                    if (result != -1) and (len(j) == result + len(sys.argv[1])):
                        available_dir[len(available_dir) + 1] = j
                except AttributeError:
                    pass
        if len(available_dir) == 1:
            os.chdir(available_dir[1])
            os.system('/bin/bash')
        elif len(available_dir) > 1:
            print('The directories which were found:')
            for number, path in available_dir.items():
                print('{}. {}'.format(number, path))
            print("{}. {}".format(number + 1, "Don\'t change directory"))
            
            available_dir[len(available_dir) + 1] = os.getcwd()
            os.chdir(available_dir[int(input(">>> "))])
            os.system('/bin/bash')
        elif len(available_dir) == 0:
            print('This directory wasnt found')
