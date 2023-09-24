### Exercise 3 - q1: Dynamic Programming ###

### Template ###

#import libraries:
import numpy as np

#a. main function

def Choose_customers(customers_lst, Patience_threshold):
    w = Patience_threshold # variable for patience
    n = len(customers_lst) # variable for number of customers
    new_array = np.zeros((n + 1, w + 1)) # building new matrix with zeroes
    for i in range(1, n + 1): # going through the rows
        for j in range(1, w + 1): # going through the columns
            if customers_lst[i - 1][0] > j: # we cant take  this customer
                new_array[i, j] = new_array[i-1, j] # we take the option without this customer
            else:
                # choosing the max value between 2 option, we take the customer not
                new_array[i, j] = max(new_array[i-1, j], new_array[i - 1, j - customers_lst[i - 1][0]] + customers_lst[i - 1][1])
    total_value = new_array[n, w] # we take the final value
    chosen_suppliers = call_back(customers_lst, new_array, Patience_threshold) # restoring the indexes of the customers in the list
    print(new_array)
    return total_value, chosen_suppliers

def call_back(lst, array, w):
    customer_lst = []
    current_w = w
    for i in range(len(lst), 0, -1): # loop for all the customers
        if array[i, current_w] != array[i-1, current_w] and current_w != 0: # check if we took the customer or not
            customer_lst.append(i - 1) # add the index to the list
            current_w -= lst[i-1][0]
    return customer_lst[::-1]


#b. subset-sum function (remember 3 code line is 3 points extra!)

def subset_sum_algo(numbers, subset_sum):
    new_lst = [(i ,i) for i in numbers] # creating list of tuples that the negative and positive values is equal
    final, lst = Choose_customers(new_lst, subset_sum) # calling
    return final == subset_sum


