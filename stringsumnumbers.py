# stringsumnumbers.py
# Raunak Anand

user_input = input("Enter a string: ")
number_sum = 0
string = ""
for character in user_input:
    if character >= "0" and character <= "9":
        string += character
    elif character == ".":
        string += character
    elif string:
        number_sum += float(string)
        string = ""

if string:
    number_sum += float(string)

print('%.2f' % number_sum) # print the sum in two decimal places


