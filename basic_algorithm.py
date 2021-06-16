import myFunctions
import PreProcess

# necessary variables and attributes
edit_operation = PreProcess.edit_operations
S = PreProcess.S
pattern_length = 10
ref_seq_B = PreProcess.ref_seq_B
pattern = myFunctions.seq_gen(7)
q_gram_length = 3

q_gram_pattern = [pattern[i:j] for i in range(len(pattern)) for j in range(i + 1, len(pattern) + 1) if
                  len(pattern[i:j]) == q_gram_length]
print(f"Pattern : {q_gram_pattern}")
q_gram_ref_seq_B = [ref_seq_B[i:j] for i in range(len(ref_seq_B)) for j in range(i + 1, len(ref_seq_B) + 1) if
                    len(ref_seq_B[i:j]) == q_gram_length]
print(f"Reference Base sequence : {q_gram_ref_seq_B}")

# foreach q-gram B[t, t + q − 1] matching a q-gram P[j, j + q − 1] do
# 4 Find those transformations T′ ∈ T that do not modify
# B[t, t + q − 1];

tranformation_list = []
operated_index = myFunctions.op_ind(edit_operation)
# print(operated_index)


for q_gram in q_gram_ref_seq_B:
    search_flag = 0
    if q_gram in q_gram_pattern:
        start_index = q_gram_ref_seq_B.index(q_gram)
        # print(q_gram,start_index)
        t_index = [ind for ind in range(start_index, start_index + q_gram_length)]
        # print(t_index)
        op = []
        for index in t_index:
            if index in operated_index.values():
                for key, val in operated_index.items():
                    if index == val:
                        op.append(key)
                        break
        # print(op)
        not_modified = [t for t in edit_operation if t not in op]
        # print(not_modified)
        # Find the lowest position l1,l2 such that B[l1:l1+q_gram_len] and P[l2:l1+q_gram_len] matches and no edit
        # operation on that part′b

        if len(not_modified) != 0:
            search_flag = 1
            for pos in not_modified:
                print(f"{q_gram} found", end=" ")
                print(f"In S : {S[pos]}")
                print(f" Position S[{S[pos].find(q_gram)}:{S[pos].find(q_gram) + q_gram_length}]")

    if search_flag == 0:
        print(f"{q_gram} is Not found")
