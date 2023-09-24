''' Exercise #4. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def most_popular_characters(my_string):
	dict_popular = {}
	most_used = []
	for char in my_string:
		if not char in dict_popular:
			dict_popular[char] = 1
		else:
			dict_popular[char] = dict_popular[char] + 1
	most_number_of_uses = max(dict_popular.values())
	for char in dict_popular:
		if dict_popular[char] == most_number_of_uses:
			most_used.append(char)
		alphabet = sorted(most_used)
	return alphabet[0]
#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):
	new_sub_mat = lst[0]
	i = 0
	for elem in lst:
		if i == 0:
			i += 1
		else:
			key = elem.keys()
			for tuple in key:
				if tuple in new_sub_mat:
					new_sub_mat[tuple] = new_sub_mat[tuple] - elem[tuple]
				else:
					new_sub_mat[tuple] = -elem[tuple]
	return new_sub_mat

#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
	substring_location = {}
	i = 0
	key = ""
	for char in s:
		if k == len(s):
			key = s
			substring_location[key] = [0]
		else:
			key = s[i : i + k]
			if len(key) == k:
				if not key in substring_location:
					substring_location[key] = [i]
				else:
					substring_location[key].append(i)
				key = ""
				i += 1
	return substring_location










#########################################
# Question 4 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):
	student_courses = {}
	for tuple in tuples_lst:
		i = 0
		for str in tuple:
			lower_str = str.lower()
			if i == 0:
				i = 1
				if lower_str in student_courses:
					student_courses[lower_str].append(tuple[1].lower())
				else:
					student_courses[lower_str] = [tuple[1].lower()]
			else:
				i = 0
	return student_courses


def num_courses_per_student(stud_dict):
	for key in stud_dict.keys():
		stud_dict[key] = len(stud_dict[key])

#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

if __name__ == '__main__': #Do not delete this line!
	# Q1
	print(most_popular_characters('gggcccbb') == 'c')

	# Q2
	print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): -4, (2, 7): 1})
		
	# Q3
	print(find_substring_locations('TTAATTAGGGGCGC', 2) == {'TT': [0, 4], 'TA': [1, 5], 'AA': [2], 'AT': [3], 'AG': [6], 'GG': [7, 8, 9], 'GC': [10, 12], 'CG': [11]})

	# Q4
	stud_dict = courses_per_student([('Tom', 'Math'), ('Oxana', 'Chemistry'), ('Scoobydoo', 'python'), ('Tom', 'pYthon'), ('Oxana', 'biology')])
		
	print(stud_dict == {'tom': ['math', 'python'], 'oxana': ['chemistry', 'biology'], 'scoobydoo': ['python']})
		
	num_courses_per_student(stud_dict)
	print(stud_dict == {'tom': 2, 'oxana': 2, 'scoobydoo': 1})


# ============================== END OF FILE =================================

