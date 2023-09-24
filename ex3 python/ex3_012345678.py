''' Exercise #3. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################

def sum_divisible_by_k(lst, k):
    sum_of_divisible = 0
    for i in lst:
        if i % k == 0:
            sum_of_divisible += i
    return sum_of_divisible






#########################################
# Question 2 - do not delete this comment
#########################################
def mult_odd_digits(n):
    num_lst = [int(x) for x in str(n)]
    mult_odd_numbers = 1
    for i in num_lst:
        if i % 2 == 1:
            mult_odd_numbers *= i
    return mult_odd_numbers




#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):
    this_repetition = 0
    longest_repetition = 0
    for i in s:
        if i == c:
            this_repetition += 1
        else:
            this_repetition = 0
        if this_repetition > longest_repetition:
            longest_repetition = this_repetition
    return longest_repetition


#########################################
# Question 4 - do not delete this comment
#########################################
def upper_strings(lst):

    if type(lst) != list:
        return -1
    else:
        for elem in lst:
            type_off = type("string")
            index = lst.index(elem)
            print(index)
            if type(elem) == type_off :






#########################################
# Question 5 - do not delete this comment
#########################################
# def div_mat_by_scalar(mat, alpha):
#     pass


#########################################
# Question 6 - do not delete this comment
#########################################
# def mat_transpose(mat):
#     pass


    
#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == '__main__':  # Do not delete this line!
    print(sum_divisible_by_k([3, 6, 4, 10, 9], 3) == 18)
    print(sum_divisible_by_k([45.5, 60, 73, 48], 4) == 108)


    print(mult_odd_digits(5638) == 15)
    print(mult_odd_digits(2048) == 1)
    print(mult_odd_digits(54984127) == 315)


    print(count_longest_repetition('eabbaaaacccaaddd', 'a') == 4)
    print(count_longest_repetition ('cccccc','c') == 6)
    print(count_longest_repetition ('abcde', 'z') == 0)


    vals = [11, 'TeSt', 3.14, 'cAsE']
    upper_strings(vals)
    print(vals == [11, 'TEST', 3.14, 'CASE'])

    vals = [-5, None, True, [1, 'dont change me', 3]]
    upper_strings(vals)
    print(vals == [-5, None, True, [1, 'dont change me', 3]])

    print(upper_strings(42) == -1)
    print(upper_strings('im not a list') == -1)
    print(upper_strings(False) == -1)


    mat1 = [[2, 4], [6, 8]]
    mat2 = div_mat_by_scalar(mat1, 2)
    print(mat1 == [[2, 4], [6, 8]])
    print(mat2 == [[1, 2], [3, 4]])

    print(div_mat_by_scalar([[10,15], [-3,6]], -5) == [[-2, -3], [0, -2]])


    mat = [[1,2],[3,4],[5,6]]
    mat_T = mat_transpose(mat)
    print(mat == [[1, 2], [3, 4], [5, 6]])
    print(mat_T == [[1, 3, 5], [2, 4, 6]])

    mat2 = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
    mat2_T = mat_transpose(mat2)
    print(mat2_T == [[0, 10, 20], [1, 11, 21], [2, 12, 22]])

# ============================== END OF FILE =================================
