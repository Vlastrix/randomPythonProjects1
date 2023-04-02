#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
len_let = len(letters)
len_num = len(numbers)
len_sym = len(symbols)
logo = """"""
print(logo)
print("Welcome to the PyPassword Generator!")
nr_letters= int(input(f"How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#use the Join Function
let_list = []
for letter in range(nr_letters): #range function by default starts from 0, don't need to specify that
    random_letter = random.randint(0, len_let - 1)
    let_list.append(letters[random_letter])
let_join_string = ''.join(map(str, let_list))


sym_list = []
for symbol in range(nr_symbols):
    random_symbol = random.randint(0, len_sym - 1)
    sym_list.append(symbols[random_symbol])
sym_join_string = ''.join(map(str, sym_list))


num_list = []
for number in range(nr_numbers):
    random_number = random.randint(0, len_num - 1)
    num_list.append(numbers[random_number])
num_join_string = ''.join(map(str, num_list))


alloflists = let_list + sym_list + num_list
len_alloflists = len(alloflists)

   
seq_password = let_join_string + sym_join_string + num_join_string #sequencial ans (easy)

password_list = []
for rand in range(len_alloflists):
    rand_pass = random.shuffle(alloflists)

for rand in range(len_alloflists): 
    rand_pass = random.shuffle(alloflists)

pass_join_string = ''.join(map(str, alloflists))
non_seq_password = pass_join_string #non sequencial answer

print(f"Your sequential password is: {seq_password}")
print(f"Your non sequential password is: {non_seq_password}")

#Ignore this part
# mylist = ["apple", "banana", "cherry"]
# random.shuffle(mylist)
#it changes the list completely --------------! Very important
# print(mylist)




