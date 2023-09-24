''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1.a - do not delete this comment
#########################################
def four_bonacci_rec(n):
    if n == 0:
        return 0
    elif n < 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return four_bonacci_rec(n-1) + four_bonacci_rec(n-2) + four_bonacci_rec(n-3) + four_bonacci_rec(n-4)

#########################################
# Question 1.b - do not delete this comment
#########################################
def four_bonacci_mem(n, memo=None):
    if n < 4:
        return n
    if memo == None:
        memo = {}
    if n not in memo:
        memo[n] = four_bonacci_rec(n-1) + four_bonacci_rec(n-2) + four_bonacci_rec(n-3) + four_bonacci_rec(n-4)
    return memo[n]



#########################################
# Question 2 - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    if n <= 0:
        return 0
    if n <= 2:
        return n
    if memo is None:
        memo = {}
    if n not in memo:
        memo[n] = climb_combinations_memo(n-1) + climb_combinations_memo(n-2)
    return memo[n]

#########################################
# Question 3 - do not delete this comment
#########################################
def catalan_rec(n,memo=None):
    if memo is None:
        memo = {}
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    res = 0
    for i in range(n):
        res += catalan_rec(i, memo) * catalan_rec(n - 1 - i, memo)
    memo[n] = res
    return res





#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    if n == 0:
        return 1
    if n < 0 or len(lst) == 0:
        return 0
    option_1 = find_num_changes_rec(n - lst[0], lst)
    option_2 = find_num_changes_rec(n, lst[1:])
    return option_2 + option_1










#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    if n == 0:
        return 1
    if n < 0 or len(lst) == 0:
        return 0
    if memo == None:
        memo = {}
    new_tuple = (len(lst), n)
    if new_tuple in memo:
        return memo[new_tuple]
    else:
        option_1 = find_num_changes_mem(n - lst[0], lst, memo)
        option_2 = find_num_changes_mem(n, lst[1:], memo)
        memo[new_tuple] = option_2 + option_1
    return option_2 + option_1

#########################################
# Question 5 - do not delete this comment
#########################################
def count_subseq(s, subseq, memo=None):
    if len(subseq) == 0:
        return 1
    if len(s) == 0:
        return 0
    if memo is None:
        memo = {}
    my_key = (len(s), subseq)
    if my_key not in memo:
        if s[-1] == subseq[-1]:
            memo[my_key] = count_subseq(s[:-1], subseq[:-1], memo) + count_subseq(s[:-1], subseq, memo)
        else:
            memo[my_key] = count_subseq(s[:-1],subseq, memo)
    return memo[my_key]


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

if __name__ == "__main__":
    #Question 1.a tests - you can and should add more

    print(four_bonacci_rec(0) == 0)
    print(four_bonacci_rec(5) == 12)
    print(four_bonacci_rec(8) == 85)
    """
    #Question 1.b tests - you can and should add more
    """
    print(four_bonacci_mem(0) == 0)
    print(four_bonacci_mem(5) == 12)
    print(four_bonacci_mem(8) == 85)
    """
    #Question 2 tests - you can and should add more
    """
    print(climb_combinations_memo(7) == 21)

    """
    #Question 3 tests - you can and should add more
    """
    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_rec(n) == res)
    """
    #Question 4.a tests - you can and should add more
    """
    print(find_num_changes_rec(5,[1,2,5,6]) == 4)
    print(find_num_changes_rec(4,[1,2,5,6]) == 3)
    print(find_num_changes_rec(0,[1,2,5,6]) == 1)
    print(find_num_changes_rec(105,[1,105,999,100]) ==3)
    """
    #Question 4.b tests - you can and should add more
    """
    print(find_num_changes_mem(5,[1,2,5,6]) == 4)
    print(find_num_changes_mem(4,[1,2,5,6]) == 3)
    print(find_num_changes_mem(105,[1,105,999,100]) ==3)
    """
    #Question 5 tests - you can and should add more
    """
    print(count_subseq("0010", "01") == 2)
    print(count_subseq("ABBABBABBABBA", "AB") == 20)
    print(count_subseq("PyCharm", "Charm") == 1)
    print(count_subseq("PyCharm", "PY") == 0)
    print(count_subseq("Cool", "") == 1)

    pass
# ============================== END OF FILE =================================
