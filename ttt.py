import random

from itertools import combinations

# all numbers allowed for input
num_array = [1,2,3,4,5,6,7,8,9]

# wining array
win_array = [
    [1,2,3],
    [1,4,7],
    [1,5,9],
    [2,5,8],
    [3,5,7],
    [3,6,9],
    [4,5,6],
    [7,8,9]
]

# no chance array
no_array = []

# list of reserved array or input chosed
res_array = []

# user input array
user_array = []

# computer input array
com_array = []

# print tic-tac-toe matrix based on user and computer input
def print_matrix():
    print()
    for i in range(1,10):
        if i in user_array:
            print('1', end=' ')
        else:
            if i in com_array:
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
    if len(user_array) == 2:
        for i in win_array:
            check = all(item in i for item in user_array)
            if check is True:
                if i in no_array:
                    pass
                else:
                    return i
    if len(user_array) > 2:
        user_move_array = sub_list(user_array)
        for i in user_move_array:
            for j in win_array:
                check = all(item in j for item in i)
                if check is True:
                    if j in no_array:
                        pass
                    else:
                        return j

# for user_input
def user_minus(fav_list):
    for i in fav_list:
        if i in user_array:
            pass
        else:
            return i

# computer self analysis array function
def self_analysis_array():
    if(len(com_array) == 1):
        for i in win_array:
            check = all(item in i for item in com_array)
            if check is True:
                flag = False
                for j in i:
                    if j in user_array:
                        flag = True
                        break
                if(flag == True):
                    pass
                else:
                    return i
    if len(com_array) > 1:
        com_move_array = sub_list(com_array)
        for i in com_move_array:
            for j in win_array:
                check = all(item in j for item in i)
                if check is True:
                    flag = False
                    for k in j:
                        if k in user_array:
                            flag = True
                            break
                    if(flag == True):
                        pass
                    else:
                        return j

def self_minus(fav_list):
    for i in fav_list:
        if i in com_array:
            pass
        else:
            return i

def minus():
    for i in num_array:
        if i in res_array:
            pass
        else:
            return i

def self_analysis():
    favourable_array = self_analysis_array()
    if favourable_array is None:
        fav_input = minus()
        com_array.append(fav_input)
        res_array.append(fav_input)
        print('Computer Input (0) => ', fav_input)
    else:
        fav_input = self_minus(favourable_array)
        com_array.append(fav_input)
        res_array.append(fav_input)
        print('Computer Input (0) => ', fav_input)

# user input function
def user_input():
    temp = int(input('User Input (1) => '))

    if temp not in num_array:
        print('*** Error in Input ***')
        user_input()
    else:
        if(temp in res_array):
            print('*** Reserved ***')
            user_input()
        else:
            user_array.append(temp)
            res_array.append(temp)

# computer first time input function
def computer_first_input():
    # most probable numbers to start to win
    temp = random.choice([1,2,3,4,7])
    com_array.append(temp)
    res_array.append(temp)
    print('Computer Input (0) => ', temp)

def computer_input():
    if(len(user_array) > 1):
        # user move analysis
        favourable_array = user_move_analysis()
        if favourable_array is None:
            # self move analysis
            self_analysis()
        else:
            fav_input = user_minus(favourable_array)
            if fav_input in res_array:
                # self move analysis
                self_analysis()
            else:
                com_array.append(fav_input)
                res_array.append(fav_input)
                no_array.append(favourable_array)
                print('Computer Input (0) => ', fav_input)
    else:
        # self move analysis
        self_analysis()

def match_computer():
    comb = list(combinations(com_array,3))
    arr = []
    for ii in comb:
        arr.append(list(ii))
    for i in win_array:
        for j in arr:
            check = all(item in i for item in j)
            if check is True:
                return True
            else:
                pass

def match_user():
    comb = list(combinations(user_array,3))
    arr = []
    for ii in comb:
        arr.append(list(ii))
    for i in win_array:
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