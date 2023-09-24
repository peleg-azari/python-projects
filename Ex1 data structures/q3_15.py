# ~~~ This is a template for question 3  ~~~

#imports
from q1_15 import merge_sort_implementation
from q2_15 import insertion_sort_implementation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
    this code loading data from outer excel file
     
    analyses and display

    the running time for sorting a list in 2 methods - 

    merge sorting and insertion sorting.
    
    """

#load data:
file = pd.ExcelFile("data_1.xlsx")
data1 = pd.read_excel(file, "data_1_1")['sort_me_1'].tolist()
data2 = pd.read_excel(file, "data_1_2")['sort_me_2'].tolist()
data3 = pd.read_excel(file, "data_1_3")['sort_me_3'].tolist()
data4 = pd.read_excel(file, "data_1_4")['sort_me_4'].tolist()
data5 = pd.read_excel(file, "data_1_5")['sort_me_5'].tolist()

#sort data and save results:
def sort_data(data):

    ##insertion sort:
    sorted_lst_insertion, counter_insertion = insertion_sort_implementation(data)

    ##merge_sort:
    sorted_lst_merge, counter_merge = merge_sort_implementation(data)
    return (counter_insertion, counter_merge)

a = sort_data(data1)
b = sort_data(data2)
c = sort_data(data3)
d = sort_data(data4)
e = sort_data(data5)


#plot figure:


# Defining the values of the bars
x = np.array([1, 2, 3, 4, 5])
y1 = np.array([a[0], b[0], c[0], d[0], e[0]])
y2 = np.array([a[1], b[1], c[1], d[1], e[1]])


# defining the width of each bar
width = 0.35

# creating plot with two bars for each x value
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, y1, width, label='Insertion sort')
rects2 = ax.bar(x + width/2, y2, width, label='Merge sort')
# defention for labling the bars
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# Adding text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('data')
ax.set_ylabel('results')
ax.set_title('number of basic operations for sorting')
ax.set_xticks(x)
ax.set_xticklabels(["data_1_1", "data_1_2", "data_1_3", "data_1_4", "data_1_5"])
ax.legend()

# Show the plot
plt.show()

