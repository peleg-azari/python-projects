# ~~~ This is a template for question 2  ~~~

#Imports:
import pandas as pd
###Part A###
#~~~  implementation of heap class  ~~~
class Heap():
    def __init__(self, A):
        self.size = len(A)
        self.t = A
        self.build_heap()

    def build_heap(self):
        """ this function implement the heapify function for

         every element in the first half of the list."""

        for i in range(self.size//2, -1, -1):
            self.heapify(i)
        return self.t

    def parent(self, i):
        """this function return fot given index his

        parent and his parent index

        input: index

        output: tuple of (parent value, parent index)"""

        # parent of list with size zero or 1 is None
        if self.size == 0 or self.size == 1:
            return None
        # if i not in the index of the list parent is None
        if i < 0 or i >= self.size:
            return None
        # checks if i is even or odd and returns his parent accordingly
        if i/2 == i//2:
            return (self.t[i//2 - 1], i//2 - 1)
        else:
            return (self.t[i//2], i//2)


    def insert(self, x):
        """this function insert the element

         x to his cooret place in the heap """

        # expand the size of the list by 1
        self.size += 1

        # adding the element x to end of the list
        self.t.append(x)

        # if x is the only element in the heap he is in the right place
        if self.size == 1:
            return

        # setting variable to the index of x
        current = self.size - 1

        # using parent function to check who is x's parent and hsi index
        par_val, par_i = self.parent(current)

        # the loop runs until x is bigger then his parent or his first in the heap
        while current > 1 and self.t[current] <= par_val:

            # replace x with his parent
            self.t[current], self.t[par_i] = par_val, self.t[current]

            # updating the variables to the next step
            current = par_i
            par_val, par_i = self.parent(par_i)


    def delete_min(self):
        """this function delete the first

         element in the heap and return his value"""

        if self.size == 0:
            return None

        # setting variable with the value of the first element
        min = self.t[0]

        # special case when size is 1
        if self.size == 1:
            self.size -= 1
            self.t = []
            return min

        # setting the first element to be the value of the last element
        self.t[0] = self.t[self.size - 1]

        # erasing the last element in the list and updating the zise of the list
        self.t = self.t[:-1]
        self.size -= 1

        # reorder the heap to correct order after the change
        self.heapify(0)

        return min

    def heapify(self,i):
        """ This function receives an index and arranges it to its

        correct place in the heap"""

        # checks if there is no elements in the list
        if self.size == 0:
          return None

        # checks if the element to order is the first one
        if i == 0:

            # if the elem is the only one he is in place
            if self.size == 1:
                return

            # checks if there is only 1 child to the firs elements
            if self.size == 2:

                # checks if his child that on the left is smaller
                left = self.t[1]
                if self.t[0] > left:

                    # switching the values of the parent and the child
                    self.t[0], self.t[1] = left, self.t[0]
                return

            # else: the parent in the index 0 have 2 kids, setting them to variables
            left = self.t[1]
            right = self.t[2]

            # checks if the parent is smaller than his childes
            if self.t[0] <= left and self.t[0] <= right:
                return

            # if not
            # checks if the left child is bigger then the right child
            if left >= right:

                #replace the parent with the right child
                self.t[0], self.t[2] = right, self.t[0]

                # A recursive call for the replaced parent in his new index
                self.heapify(2)
            else:

                # replace the parent with the left child
                self.t[0], self.t[1] = left, self.t[0]

                # A recursive call for the replaced parent in his new index
                self.heapify(1)

        # checks if the element is in the lowest row of the heap
        if self.size <= i*2 + 1:
            return

        # checks if the element only have left child
        if self.size == i*2 + 2:

            # checks if his left child smaller then him
            left = self.t[i*2+1]
            if left < self.t[i]:

                # replace between them
                self.t[i], self.t[i*2+1] = left, self.t[i]
            return

        # else, there is 2 childes for him
        left = self.t[i*2 + 1]
        right = self.t[i*2 + 2]

        # checks if the parent is smaller than his childes
        if self.t[i] <= left and self.t[i] <= right:
            return

        # else, checks if the left child is bigger the right child
        elif left >= right:

            # switch between the parent and the right child
            self.t[i], self.t[i*2+2] = right, self.t[i]

            # A recursive call for the replaced parent in his new index
            self.heapify(i*2+2)
        else:

            # switch between the parent and the left child
            self.t[i], self.t[i*2+1] = left, self.t[i]

            # A recursive call for the replaced parent in his new index
            self.heapify(i * 2 + 1)


##Part B###
def optimal_value_merge_problem(prices):
    """ this function merge prices and calculate the overall taxes to pay

    input: list of numbers
                (int or floats)

    output: taxes to pay
                (number - int or float)

    """

    # if the list is empty, no taxes to pay
    if len(prices) == 0:
        return 0

    # if there is 1 number in the list, no taxes to pay
    if len(prices) == 1:
        return 0

    # transfer the list to a heap class
    tree = Heap(prices)

    # new variable to the overall taxes
    tax = 0

    # loop until the heap have 1 element
    while tree.size > 1:

        # use delete.min function to delete the 2 smallest numbers in
        # the heap and sett them into variables
        min1 = tree.delete_min()
        min2 = tree.delete_min()

        # sum the tax for the murge
        tax += min1 + min2

        # insert back to the heap the merged company
        tree.insert(min1 + min2)

    return tax

def excel_to_list(file):
    """ this function gets an excel file name and

     extract from it data to a list using pandas

     input: string

     output: list

     """

    # transfer the excel file into pandas data frame
    df = pd.read_excel(file)

    # extract only the first column with the prices
    tax = df.iloc[:,0]

    # transfer the column into a list
    lst_prices = tax.tolist()

    return lst_prices

lst = excel_to_list("data_2.xlsx")
print(optimal_value_merge_problem(lst))
