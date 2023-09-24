''' Exercise #5. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def rixum(file_name):
     def is_digit(i):
         return i.isdigit()
     def last_num(elem):
         for i in range(len(elem), 0, -1):
             if not is_digit(elem[i -1]):
                 return elem[i:]
         return elem
     f = open(file_name, 'r')
     s = f.read()
     tabs = s.split(" ")
     result = 0
     for elem in tabs:
         result += int(last_num(elem))
     f.close()
     return result
#########################################
# Question 2 - do not delete this comment
#########################################
def rickounter(f_document, f_rick_identifiers):
    f = open(f_rick_identifiers, 'r')
    lines = []
    for line in f:
        new_line = line.strip()
        lines.append(new_line)
    f.close()
    d = open(f_document, 'r')
    s = d.read()
    d.close()
    def in_document(str, substr):
        n1 = len(str)
        n2 = len(substr)
        if n1 == 0 or n1 < n2:
            return 0
        if str[:n2] == substr:
            return in_document(str[1:],substr) + 1
        return in_document(str[1:],substr)
    count = {}
    for elem in lines:
        count[elem] = in_document(s, elem)
    return count
#########################################
# Question 3 - do not delete this comment
#########################################
def twin_pricks(num, out_file_name):
    f = open(out_file_name, 'w')
    def build_twin_Primes_nums(n):
        primes = []
        twins = []
        for num in range(n):
            if num <= 1:
                continue
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
        for prime in primes:
            if primes.index(prime) >= 1:
                if prime - primes[primes.index(prime) - 1] == 2:
                    twins.append((primes[primes.index(prime) - 1], prime))
        return twins
    def check_twin_primes_num(num, n=0):
        if num == len(build_twin_Primes_nums(n)):
            return build_twin_Primes_nums(n)
        return check_twin_primes_num(num, n + 1)
    def write_str(lst):
        string = ""
        for elem in lst[:-1]:
                string = string + str(elem[0]) + "," + str(elem[1]) + "\n"
        string += str(lst[-1][0]) + "," + str(lst[-1][1])
        return string
    f.write(write_str(check_twin_primes_num(num)))
    f.close()





#########################################
# Question 4 - do not delete this comment
#########################################
def rickode(in_file):
    f = open(in_file, 'r')
    s = f.read()
    rep_str = ''
    for letter in s:
            if letter.isalpha() == True:
                if letter == "y":
                    rep_str += "a"
                elif letter == "Y":
                    rep_str += "A"
                elif letter == "Z":
                    rep_str += "B"
                elif letter == "z":
                    rep_str += "b"
                else:
                    code = ord(letter)
                    nxt_letter = chr(code + 2)
                    rep_str = rep_str + nxt_letter
            else:
                rep_str += letter
    f.close()
    name_of_new = in_file[:str.rfind(in_file, ".")] + "_decipherick" + in_file[str.rfind(in_file, "."):]
    w = open(name_of_new, 'w')
    w.write(rep_str)
    w.close()
    return name_of_new
#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    NO_EXC_MSG="Exception must be raised for this input (NOT pass)."
    WRONG_EXC_MSG="Wrong message in raised exception (NOT pass). \nExpected: {}\nGot: {}\n"
    NOT_PASS_MSG="Unexpected result (NOT pass.)"

    PASS_MSG="Got expected results (pass)."
    EXPECTED_EXC_MSG="Got corrent error and error message (pass)."
    

    print('==== Q1: Basic tests/output====')
    q1_input_file_name = "q1_input_1.txt"
    expected_result=137
    actual_result=rixum(q1_input_file_name)
    print("q1t1:", f'{PASS_MSG if expected_result==actual_result else NOT_PASS_MSG}')
    print("TBD: It is recommended to write here more tests of your own")
    
    print('==== Q2: Basic tests/output====')
    expected_result={'Hello_word9': 0, 'CoolRick11': 1, 'C-137': 2, 'c-132': 1, 'Z0Zo0': 1, 'TestMeRick123': 1}
    actual_result=rickounter("q2_f_document_1.txt", "q2_f_rick_identifiers_1.txt")
    print("q2t1", f"{(PASS_MSG if expected_result==actual_result else NOT_PASS_MSG)}")
    if expected_result!=actual_result:
        print(f'Expected: {expected_result}')
        print(f'Got: {actual_result}')

    expected_result = {"Larry12": 0, "david94": 0, "33": 5}
    actual_result = rickounter("q2_f_document_2.txt", "q2_f_rick_identifiers_2.txt")
    print("q2t2", f"{(PASS_MSG if expected_result == actual_result else NOT_PASS_MSG)}")
    if expected_result != actual_result:
        print(f'Expected: {expected_result}')
        print(f'Got: {actual_result}')

    print('==== Q3: Basic tests/output====')
    twin_pricks(4, "q3_output_1_res.txt")
    expected_result=open('q3_output_1_sol.txt', 'r').read()
    actual_result=open('q3_output_1_res.txt', 'r').read()
    print("q3t1", f"{(PASS_MSG if expected_result==actual_result else NOT_PASS_MSG)}")
    if expected_result!=actual_result:
        print(f'Expected: \n{expected_result}')
        print(f'Got: \n{actual_result}')

    twin_pricks(20, "q3_output_2_res.txt")
    expected_result=open('q3_output_2_sol.txt', 'r').read()
    actual_result=open('q3_output_2_res.txt', 'r').read()
    print("q3t2", f"{(PASS_MSG if expected_result==actual_result else NOT_PASS_MSG)}")
    if expected_result!=actual_result:
        print(f'Expected: \n{expected_result}')
        print(f'Got: \n{actual_result}')

    print('==== Q4: Basic tests/output====')
    q4_input_file_name = "q4_input_1.txt"
    deciphered_text="There's a lesson here, and I'm not going to be the one to figure it out\n\nAnd...\n\nThere'Z a lesson here, and I'm not going to be the one to figure it out!!"
    with open(rickode(q4_input_file_name),'r') as f:
        print(f'{PASS_MSG if f.read() == deciphered_text else NOT_PASS_MSG}')



   

# ============================== END OF FILE =================================
