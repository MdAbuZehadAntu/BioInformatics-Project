import numpy as np
import random

from random import choice

alphabet_set = 'ATCG'  # for DNA


# random DNA sequence generation
def seq_gen(length, seq_num):
    for i in range(seq_num):
        DNA = ""
        for count in range(length):
            DNA += choice(alphabet_set)

    return DNA


# edit_operation generation
def edit_op(edit_options, B, n):
    edit_operations = dict()
    for i in range(n):
        small_dict = {"operation": "", "index": "", "char": ''}

        edit_pos = random.randint(0, len(B) - 1)

        small_dict['operation'] = random.choice(edit_options)
        small_dict['index'] = edit_pos

        edit_operations[i] = small_dict
    return edit_operations


# a collection of sequence S generation
def S_generation(B, edit_op):
    s_list = list()
    for i in range(len(edit_op)):

        temp = B
        index = edit_op[i]['index']
        if edit_op[i]['operation'] == 'insert':
            char = choice(alphabet_set)
            temp = temp[:edit_op[i]['index']] + char + temp[edit_op[i]['index']:]
            s = temp
            edit_op[i]['char'] = char
            edit_op[i]['index'] = index
            s_list.append(s)

        elif edit_op[i]['operation'] == 'delete':
            char = temp[edit_op[i]['index']]
            temp = temp[:edit_op[i]['index']] + temp[edit_op[i]['index'] + 1:]
            s = temp
            edit_op[i]['char'] = char
            edit_op[i]['index'] = index
            s_list.append(s)
        else:
            char = choice(alphabet_set)
            temp = temp[:edit_op[i]['index']] + char + temp[edit_op[i]['index'] + 1:]
            s = temp
            edit_op[i]['char'] = char
            edit_op[i]['index'] = index
            s_list.append(s)

    return s_list,edit_op
