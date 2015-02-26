'''
AiEura is a chatbot that learns from communication.
The more AiEura is talked to, the better it can communicate.
Features
    - Checks dictionary for words.
    - Has wordfilter to prevent contamination.
    - Words can be learned or added to the dictionary.
    - Can learn to communicate in any lanugage.
    - All memory is easily accessible in one file.
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

def proc_line(x,y):
    # removes syntax from save file and sorts line types
    # x is the list
    # y is the type
    #     0 for dialog
    #     1 for response
    #     2 for total
    z = []
    if y is 0:
        for each in x:
            if len(each) > 0:
                if each[0] is '-':
                    z.append(each[1:-1])
    if y is 1:
        for each in x:
            if len(each) > 0:
                if each[0] is '=':
                    z.append(each[1:-1])
    if y is 2:
        for each in x:
            if len(each) > 0:
                if each[0] in '-=':
                    z.append(each[1:-1])
    return z

def save_line(x,y,z):
    # x is the dialog
    # y is the response
    # z is the list
    # # print(' >> dialog: ' + x)
    # # print(' >> respon: ' + y)
    exist = 0
    for each in z:
        if exist == 0:
            if len(each) > 0:
                if each[0] is '-':
                    if each[1:-1] == x:
                        exist = 1
    if exist == 0:
        z.append('-' + x + '\n')
        z.append('=' + y + '\n')
    count = 0
    log = 0
    if exist == 1:
        k = z
        for each in k:
            if len(each) > 0:
                if each[0] is '-':
                    if each[1:-1] == x:
                        log = count
                        k = k[count+1:]
            count += 1
        # # print(k)
        count = 0
        for each in k:
            if len(each) > 0:
                if each[0] is '-':
                    k = k[:count]
            count += 1
        # # print(k)
        exist_two = 0
        for each in k:
            if len(each) > 0:
                if each[0] is '=':
                    if each[1:-1] == y:
                        exist_two = 1
        if exist_two == 0:
            z.insert(log+1,'=' + y + '\n')
    f = open('memory/data.txt', 'w')
    for each in z:
        f.write(each)
    f.close()

def save_word(x):
    f = open('memory/dict.txt', 'a')
    f.write(x + '\n')
    f.close()
    # save dictionary from file
    return
    
def gene_line(x,y,z):
    # choose a random line based on input
    # # print(' >> input: ' + x)
    x = x.split(' ')
    score = 0
    log = ''
    # # print(z)
    for each in z:
        current = 0
        test = each.split(' ')
        for every in test:
            for item in x:
                if every == item:
                    current += 1
        if current > score:
            log = each
            score = current
    x = log
    # # print(' >> ' + x)
    count = 0
    valid = 0
    for each in y:
        if valid is 0:
            if len(each) > 0:
                if each[0] is '-':
                    if each[1:-1] == x:
                        valid = 1
                        y = y[count:]
            count += 1
        if count == len(y)-1:
            valid = 2
    if valid == 1:
        count = 0
        valid = 0
        for each in y:
            if valid is 0:
                if len(each) > 0:
                    if each[0] is '-':
                        if each[1:-1] == x:
                            pass
                        else:
                            valid = 1
                            y = y[1:count]
                count += 1
        y = proc_line(y,1)
        # # print(y)
        y = y[random.randint(0,len(y)-1)]
        return y
    else:
        return 1
    
def find_fail(x,y):
    z = []
    for each in x:
        if each + '\n' in y:
            pass
        else:
            z.append(each)
    return z
    
def find_winn(x,y):
    z = []
    for each in x:
        if each + '\n' in y:
            z.append(each)
        else:
            pass
    return z

def eval_line(z):
    if len(z) > 0: return 0
    else: return 1

def chec_memo():
    if not os.path.exists('memory'):
        os.makedirs('memory')
        file_make = open('memory/data.txt', 'w')
        file_make.write('-how are you doing\n')
        file_make.close()
        file_make = open('memory/dict.txt', 'w')
        file_make.write('\n')
        file_make.close()
        file_make = open('memory/spam.txt', 'w')
        file_make.write('\n')
        file_make.close()

def rest_prog():
    python = sys.executable
    os.execl(python, python, * sys.argv)
        
# check if memory exists, if not create it
chec_memo()

# load data and dictionaries
list_line = load_file('data.txt')
list_dict = load_file('dict.txt')
list_spam = load_file('spam.txt')
print('\n >> ' + str(len(list_dict)) + ' dictionary words loaded')
print(' >> ' + str(len(list_spam)) + ' banned words loaded')
print(' >> ' + str(len(proc_line(list_line,0))) + ' dialogs loaded')
print(' >> ' + str(len(proc_line(list_line,1))) + ' responses loaded\n')
tota_list = proc_line(list_line,2)
rand_line = ''
user_save = 'user'
eura_save = ''
text_turn = 'user'   

# start the program
while 1:
    if user_save == '':
        #print(tota_list)
        rand_line = tota_list[random.randint(0,len(tota_list)-1)]
        print('  eura >> ' + rand_line)
        eura_save = rand_line
        text_turn = 'user'
    if text_turn == 'eura':
        rand_line = gene_line(user_save,list_line,proc_line(list_line,0))
        if rand_line == 1:
            rand_line = tota_list[random.randint(0,len(tota_list)-1)]
        else:
            pass
        print('  eura >> ' + rand_line)
        eura_save = rand_line
        text_turn = 'user'
    else:
        valid = 0
        while valid == 0:
            user_line = input('  user >> ')
            if user_line == '!':
                    os.system('cls')
                    rest_prog()
            user_line = user_line.lower()
            user_line = list(user_line)
            user_line = ''.join(c for c in user_line if c in 'abcdefghijklmnopqrstuvwxyz ')
            user_line = user_line.split(' ')
            temp_hold = find_fail(user_line,list_dict)
            valid = eval_line(temp_hold)
            temp_spam = find_winn(temp_hold,list_spam)
            if '' in temp_hold:
                valid = 2
            if len(temp_spam) > 0:
                temp_disp = ' '.join(c for c in temp_spam)
                print('  >> The following words have been banned from use.')
                print('  >> ' + temp_disp + '\n')
                valid = 2
            if valid == 0:
                temp_disp = ' '.join(c for c in temp_hold)
                print('  >> The following words were not found in any dictionary.')
                print('  >> ' + temp_disp)
                for each in temp_hold:
                    save_conf = input('  >> Add [' + each + '] to the dictionary?: ')
                    if save_conf in 'yesYes':
                        save_word(each)
                        list_dict = load_file('dict.txt')
                        print(' >> [' + each + '] has been added to the dictionary.\n')
                    else:    
                        print(' >> Dictionary has not been changed.\n')
            if valid == 2:
                valid = 0
        user_line = ' '.join(c for c in user_line)
        save_line(eura_save,user_line,list_line)
        list_line = load_file('data.txt')
        tota_list = proc_line(list_line,2)
        user_save = user_line
        # # print('  user >> ' + str(user_line))
        text_turn = 'eura'
