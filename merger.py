'''
AiEura file merger
Merges 2 files named data.txt and data2.txt
'''
import random
import os
import sys


def load_file(x):
    # loads memory file for conversation
    file_open = open('memory/' + x, 'r')
    list_line = file_open.readlines()
    file_open.close()
    return list_line

def process_list(x):
    total = []
    temp = []
    major = []
    minor = []
    for each in x:
        if each[0] == '-':
            if len(major) == 0:
                major.append(each[0:])
            else:
                minor.sort()
                temp.append(major)
                temp.append(minor)
                total.append(temp)
                minor = []
                major = []
                temp = []
                major.append(each[0:])
        elif each[0] == '=':
            if len(major) > 0:
                minor.append(each[0:])
    total.sort()
    return total

def chec_memo():
    if not os.path.exists('memory'):
        os.makedirs('memory')
        file_make = open('memory/data.txt', 'w')
        file_make.write('-how are you doing\n')
        file_make.close()
        file_make = open('memory/data2.txt', 'w')
        file_make.write('-how are you doing\n')
        file_make.close()
        file_make = open('memory/dict.txt', 'w')
        file_make.write('\n')
        file_make.close()
        file_make = open('memory/spam.txt', 'w')
        file_make.write('\n')
        file_make.close()

def merger(x,y):
    z = x+y
    print(z)
    total = []
    bump = []
    temp = []
    major = []
    minor = []
    for each in z:
        if len(major) == 0:
            if each[0][0] in temp:
                pass
            else:
                temp.append(each[0][0])
                major.append(each[0][0])
                print(major)
                for every in each[1]:
                    minor.append(every)
                for item in z:
                    if item[0] == major:
                        for every in item[1]:
                            if every in minor: pass
                            else:
                                minor.append(every)
                minor.sort()
                bump = major+minor
                total.append(bump)
                major = []
                minor = []
    total.sort()
    return total

def save_list(x):
    f = open('memory/merged_data.txt', 'w')
    for each in x:
        for every in each:
           f.write(every)
    f.close()
        
# check if memory exists, if not create it
chec_memo()

# load data and dictionaries
list_line = load_file('data.txt')
list_line2 = load_file('data2.txt')

# process both lists and turn them into arrays
list_array = process_list(list_line)
list_array2 = process_list(list_line2)
print(list_array)
print(list_array2)

this = merger(list_array,list_array2)
print(this)
save_list(this)
