''' Exercise #5. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[0:-1])

#########################################
# Question 2 - do not delete this comment
#########################################
def find_abs_maximum(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        if abs(lst[0]) <= abs(lst[1]):
            return lst[1]
        else: return lst[0]
    else:
        maximum = find_abs_maximum(lst[:-1])
        if abs(lst[-1]) >= abs(maximum):
            if abs(lst[-1]) == abs(maximum):
                if lst[-1] < maximum:
                    return find_abs_maximum(lst[:-1])
                else:
                    return lst[-1]
            else:
                return lst[-1]
        else:
            return maximum
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    if len(s) <= 2:
        if s[0] == s[-1]:
            return True
        return False
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    if n == 5:
        return 9
    if n == 2:
        return 2
    if n == 1:
        return 1
    if n <= 0:
        return 0
    return climb_combinations(n-1) + climb_combinations(n-2) + climb_combinations(n-5)



#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt = 0):
    if len(s) == 0:
       return cnt == 0
    if cnt < 0:
        return False
    if s[0] == "(":
        return is_valid_paren(s[1:], cnt + 1)
    elif s[0] == ")":
        return is_valid_paren(s[1:], cnt - 1)
    return is_valid_paren(s[1:], cnt)


#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == "__main__":
    #you can add tests for your code here.

    print(reverse_string("abc") == 'cba')
    print(reverse_string("Hello!") == '!olleH')

    print(find_abs_maximum([-10, 9,3,0,10]) == 10)
    print(find_abs_maximum([9,3,0]) == 9)
    print(find_abs_maximum([]) == None)
    print(find_abs_maximum([9, 3, 0, 10, 10]) == 10)
    print(find_abs_maximum([-7, 9, 3, 0, 10]) == 10)
    print(find_abs_maximum([-10, 9, 3, 0]) == -10)
    print(find_abs_maximum([-10, 10, 10, -10, 9, 3, 0]) == 10)
    print(find_abs_maximum([0]) == 0)

    print(is_palindrome("aa") == True)
    print(is_palindrome("aa ") == False)
    print(is_palindrome("caca") == False)
    print(is_palindrome("abcbbcba") == True)
    print(is_palindrome("abcbbcbA") == False)

    print(climb_combinations(3) == 3)
    print(climb_combinations(5) == 9)
    print(climb_combinations(10) == 128)

    print(is_valid_paren("(.(a)") == False)
    print(is_valid_paren("p(()r((0)))") == True)
    print(is_valid_paren("))((") == False)
    print(is_valid_paren("") == True)

# ============================== END OF FILE =================================
