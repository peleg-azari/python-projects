# ~~~ This is a template for question 2  ~~~

#implementation of insertion sort






#this function gets a list and uses insertion sort
def insertion_sort_implementation(input = list):
    """
       This function implements the insertion sort algorithm to sort an input list of elements.

       Parameters:
        --------
        input (list): The list of elements to be sorted.

       Returns:
        -------
        tuple: A tuple containing the sorted list and the number of basic operations performed during the sorting process.

       """
    # Copy the input list to a new list
    sorted_array = input

    # Initialize a variable to keep count of the number of basic operations
    number_of_basic_operations = 0

    for j in range(1, len(sorted_array)):
        # store the j-th number and the index before him in a variables
        number_of_basic_operations += 2
        newnum = sorted_array[j]
        i = j - 1

        number_of_basic_operations += 2  # 2 basic operations for the next while loop

        while(i > -1 and newnum < sorted_array[i]):
            """ 
            this loop finds the correct index to place the j-th
            number and moves all the numbers before him one place forward.
             
            newnum: the number to be sorted
             
            i: the index that is checked
             
            """

            # number that is bigger then the sorted number moves 1 place forward
            number_of_basic_operations += 2
            sorted_array[i + 1] = sorted_array[i]
            # moving 1 index backwards
            number_of_basic_operations += 1
            i = i - 1
            number_of_basic_operations += 2 # 2 basic operations for the next check on the while loop

        # placing the sorted number after the number that is smaller then him
        number_of_basic_operations += 2
        sorted_array[i + 1] = newnum
    # return the sorted list and the number of basic operations
    return sorted_array, number_of_basic_operations



