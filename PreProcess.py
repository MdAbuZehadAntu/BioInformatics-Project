import myFunctions
import random

while True:
    try:
        # S = myFunctions.seq_gen(int(input("Length of each sequence :  ")))
        ref_seq_B = myFunctions.seq_gen(20)
        break
    except Exception as e:
        print("Invalid input!!!")
if __name__ == "__main__":
    print(f"Reference sequence B : {ref_seq_B}")
    print(f"Length of the Reference sequence B : {len(ref_seq_B)}")
edit_options = ['insert', 'delete', 'substitute']
S_num = 5
edit_operations = myFunctions.edit_op(edit_options, ref_seq_B, S_num)

# a collection of sequence S
S, edit_operations = myFunctions.S_generation(ref_seq_B, edit_operations)
if __name__ == "__main__":
    print("Edit operations : ", edit_operations)
    print(S)

# print(S)
