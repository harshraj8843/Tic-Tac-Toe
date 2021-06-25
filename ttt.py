import random

from itertools import combinations

# all numbers allowed for input
num_list = [1,2,3,4,5,6,7,8,9]

# wining list
win_list = [
    [1,2,3],
    [1,4,7],
    [1,5,9],
    [2,5,8],
    [3,5,7],
    [3,6,9],
    [4,5,6],
    [7,8,9]
]

# no chance list
no_list = []

# list of reserved list or input chosed
res_list = []

# user input list
user_list = []

# computer input list
com_list = []

# print tic-tac-toe matrix based on user and computer input
def print_matrix():
    print()
    for i in range(1,10):
        if i in user_list:
            print('1', end=' ')
        else:
            if i in com_list:
                print('0', end=' ')
            else:
                print('-', end=' ')
        if i in [3,6]:
            print()
    print()
    print()

# sublist function
def sub_list (list):
    temp_list = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if i == j:
                pass
            else:
                temp_list.append([list[i], list[j]])
    return(temp_list)

# user move analysis
def user_move_analysis():
    if len(user_list) == 2:
        for i in win_list:
            check = all(item in i for item in user_list)
            if check is True:
                if i in no_list:
                    pass
                else:
                    return i
    if len(user_list) > 2:
        user_move_list = sub_list(user_list)
        for i in user_move_list:
            for j in win_list:
                check = all(item in j for item in i)
                if check is True:
                    if j in no_list:
                        pass
                    else:
                        return j

# for user_input
def user_minus(fav_list):
    for i in fav_list:
        if i in user_list:
            pass
        else:
            return i

# computer self analysis list function
def self_analysis_list():
    if(len(com_list) == 1):
        for i in win_list:
            check = all(item in i for item in com_list)
            if check is True:
                flag = False
                for j in i:
                    if j in user_list:
                        flag = True
                        break
                if(flag == True):
                    pass
                else:
                    return i
    if len(com_list) > 1:
        com_move_list = sub_list(com_list)
        for i in com_move_list:
            for j in win_list:
                check = all(item in j for item in i)
                if check is True:
                    flag = False
                    for k in j:
                        if k in user_list:
                            flag = True
                            break
                    if(flag == True):
                        pass
                    else:
                        return j

def self_minus(fav_list):
    for i in fav_list:
        if i in com_list:
            pass
        else:
            return i

def minus():
    for i in num_list:
        if i in res_list:
            pass
        else:
            return i

def self_analysis():
    favourable_list = self_analysis_list()
    if favourable_list is None:
        fav_input = minus()
        com_list.append(fav_input)
        res_list.append(fav_input)
        print('Computer Input (0) => ', fav_input)
    else:
        fav_input = self_minus(favourable_list)
        com_list.append(fav_input)
        res_list.append(fav_input)
        print('Computer Input (0) => ', fav_input)

# user input function
def user_input():
    temp = int(input('User Input (1) => '))

    if temp not in num_list:
        print('*** Error in Input ***')
        user_input()
    else:
        if(temp in res_list):
            print('*** Reserved ***')
            user_input()
        else:
            user_list.append(temp)
            res_list.append(temp)

# computer first time input function
def computer_first_input():
    # most probable numbers to start to win
    temp = random.choice([1,2,3,4,7])
    com_list.append(temp)
    res_list.append(temp)
    print('Computer Input (0) => ', temp)

def computer_input():
    if(len(user_list) > 1):
        # user move analysis
        favourable_list = user_move_analysis()
        if favourable_list is None:
            # self move analysis
            self_analysis()
        else:
            fav_input = user_minus(favourable_list)
            if fav_input in res_list:
                # self move analysis
                self_analysis()
            else:
                com_list.append(fav_input)
                res_list.append(fav_input)
                no_list.append(favourable_list)
                print('Computer Input (0) => ', fav_input)
    else:
        # self move analysis
        self_analysis()

def match_computer():
    comb = list(combinations(com_list,3))
    arr = []
    for ii in comb:
        arr.append(list(ii))
    for i in win_list:
        for j in arr:
            check = all(item in i for item in j)
            if check is True:
                return True
            else:
                pass

def match_user():
    comb = list(combinations(user_list,3))
    arr = []
    for ii in comb:
        arr.append(list(ii))
    for i in win_list:
        for j in arr:
            check = all(item in i for item in j)
            if check is True:
                return True
            else:
                pass

# main function for each input
i=0
while(i < 9):
    i = i+1
    if(i%2==0):
        user_input()
        print_matrix()
        com_done = match_user()
        if com_done == True:
            print()
            print('*****************************')
            print()
            print('********* User Won **********')
            print()
            print('*****************************')
            print()
            break
    else:
        if(i == 1):
            computer_first_input()
            print_matrix()
        else:
            computer_input()
            print_matrix()
            com_done = match_computer()
            if com_done == True:
                print()
                print('*****************************')
                print()
                print('******* Computer Won ********')
                print()
                print('*****************************')
                print()
                break