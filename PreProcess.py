import myFunctions
import random

while True:
    try:
        # S = myFunctions.seq_gen(int(input("Length of each sequence :  ")),int(input("Number of sequences : ")))
        ref_seq_B = myFunctions.seq_gen(20, 1)
        break
    except Exception as e:
        print("Invalid input!!!")

print(f"Reference sequence B : {ref_seq_B}")
pattern_length = 4
edit_options = ['insert', 'delete', 'substitute']
S_num = 5
edit_operations = myFunctions.edit_op(edit_options, ref_seq_B, 5)

# a collection of sequence S
S, edit_operations = myFunctions.S_generation(ref_seq_B, edit_operations)
print("Edit operations : ", edit_operations)
print(S)

# ref_seq_B =


# target_pattern = [dna_seq[i:j] for i in range(len(dna_seq)) for j in range(i+1,len(dna_seq)+1) if len(dna_seq[i:j])==length]
# print(S)
