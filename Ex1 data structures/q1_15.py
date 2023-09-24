# ~~~ This is a template for question 1  ~~~

#implementation of merge sort






#this function gets a list and uses merge sort
def merge_sort_implementation(_input = list):
    """
    This function sorts a list of elements using the Merge Sort algorithm.
     It recursively divides the list into two halves, sorts them, and then merges them back into a single sorted list.

    Parameters:
    ----------
    _input (list): List of elements to be sorted.

    Returns:
    ----------
    tuple: A tuple containing the sorted list and the number of basic operations performed during the sorting process.

    """

    sorted_array = _input

    # Initialize a variable to keep count of the number of basic operations
    number_of_basic_operations = 0

    number_of_basic_operations += 1
    if len(sorted_array) > 1:

        # Finding the mid of the array
        number_of_basic_operations += 1
        mid = len(sorted_array) // 2

        # Dividing the array elements
        L = sorted_array[:mid]
        number_of_basic_operations += len(L)
        # into 2 halves
        R = sorted_array[mid:]
        number_of_basic_operations += len(R)

        # Sorting the first half
        left_sorted, left_ops = merge_sort_implementation(L)

        # Sorting the second half
        right_sorted, right_ops = merge_sort_implementation(R)

        number_of_basic_operations += right_ops + left_ops

        i = j = k = 0

        # merging the 2 sorted list into 1 list
        number_of_basic_operations += 2
        while i < len(left_sorted) and j < len(right_sorted):
            number_of_basic_operations += 2
            if left_sorted[i] <= right_sorted[j]:
                sorted_array[k] = left_sorted[i]
                i += 1
            else:
                sorted_array[k] = right_sorted[j]
                j += 1
            k += 1
            number_of_basic_operations += 2 # for the next check on the while loop

        # Checking if any element was left
        number_of_basic_operations += 1
        while i < len(left_sorted):
            number_of_basic_operations += 1
            sorted_array[k] = left_sorted[i]
            i += 1
            k += 1
            number_of_basic_operations += 1 # for the next check on the while loop
        number_of_basic_operations += 1
        while j < len(R):
            number_of_basic_operations += 1
            sorted_array[k] = right_sorted[j]
            j += 1
            k += 1
            number_of_basic_operations += 1 # for the next check on the while loop

    return sorted_array, number_of_basic_operations



