""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################
# Write the rest of the code for question 1 below here.
a = 3  # Replace the assignment with a positive integer to test your code.
lst = [1, 2, 3, 4, 5]  # Replace the assignment with other lists to test your code.
i = 0
for num in lst:
    if num % a == 0:
        print(lst.index(num))
        i = i + 1
        break
if i == 0:
    print(-1)








# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
lst2 = ['hello', 'world', 'course', 'python', 'day','homework']
# Replace the assignment with other lists of strings (str) to test your code.






# Write the code for question 2 using a for loop below here.
num_of_shorter = 0
partial_sum = 0
for elem in lst2:
    partial_sum =  partial_sum + len(elem)
average = partial_sum / len(lst2)
for elem in lst2:
    if len(elem) < average:
        num_of_shorter = num_of_shorter + 1
print("The number of strings shorter than the average is:", num_of_shorter )
# Write the code for question 2 using a while loop below here.
partial_sum = 0
num_of_shorter = 0
i = 0
index = 0

while i < len(lst2):
    length = len(lst2[index])
    partial_sum = partial_sum + length
    average = partial_sum / len(lst2)
    i = i + 1
    index = index + 1

index = 0
i = 0
while i < len(lst2) :
    length = len(lst2[index])
    index = index + 1
    i += 1
    if length < average :
        num_of_shorter += 1
print("The number of strings shorter than the average is:", num_of_shorter )


# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

lst3 = [9, 6, 0, 3]  # Replace the assignment with other lists to test your code.
kefel = 1
kefel_list = []
if len(lst3) <= 1:
    if len(lst3) < 1:
        print(1)
    else:
        print(lst3[0])
if len(lst3) > 1:
    for i in lst3[0:-1]:
        sum_of_2 = i + lst3[i+1]
        i = i + 1
        kefel_list.insert(0, sum_of_2)
    for i in kefel_list[0:-1]:
        kefel = kefel * i
    print(kefel)

# Write the rest of the code for question 3 below here.



# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

lst4 = [1, 4, 8, 3, 9, 10]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.
lst_digets = [lst4[0]]
this_minus = 0
minus_pervious_lst = [0]
index = 0
for i in lst4[0:-1]:
    this_minus = abs(i - lst4[index + 1])
    index += 1
    if this_minus > max(minus_pervious_lst):
        lst_digets.append(lst4[index])
    minus_pervious_lst.append(this_minus)
print(lst_digets)
# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaadddefgggg'  # Replace the assignment with other strings to test your code.
k = 2  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.

for i in my_string:
    if i * k in my_string:
        print(F"For length {k}, found the substring {i * k}!" )
        break
else:
    print(F"Didn't find a substring of length {k}")




# End of code for question 5
