# ~~~ This is a template for question 4 (bonus)  ~~~

#implementation of selection sort






#this function gets a list and uses selection sort
def selection_sort_implementation(input = list):
    """
    Sorts a list using the selection sort algorithm.

    Parameters:
    -----------
    input : list
        The list of elements to be sorted.

    Returns:
    --------
    tuple
        A tuple containing the sorted list and the number of operations performed by the algorithm.

    """
    sorted_array = input
    # Initialize a counter variable to keep track of the number of operations performed by the algorithm
    number_of_basic_operations = 0

    # Iterate over each element in the list
    for i in range(len(sorted_array)):
        # Initialize a variable to keep track of the index of the minimum element in the unsorted part of the list
        min_idx = i

        # Increment the counter by 1 for iteration of the outer loop
        number_of_basic_operations += 1

        # Iterate over the remaining unsorted elements in the list to find the index of the minimum element
        for j in range(i + 1, len(sorted_array)):
            # Increment the counter by 3, 2 for each iteration of the inner loop and 1 for the next if statement
            number_of_basic_operations += 3

            # If the current element is smaller than the minimum element, update the index of the minimum element
            if sorted_array[min_idx] > sorted_array[j]:
                min_idx = j
                # Increment the counter by 1 for each time the index of the minimum element is updated


        # Swap the minimum element with the first unsorted element in the list
        sorted_array[i], sorted_array[min_idx] = sorted_array[min_idx], sorted_array[i]
        # Increment the counter by 2, 1 for each swap
        number_of_basic_operations += 2

    # Return a tuple containing the sorted list and the total number of operations performed by the algorithm
    return sorted_array, number_of_basic_operations

