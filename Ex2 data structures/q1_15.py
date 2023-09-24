# ~~~ This is a template for question 1  ~~~

#Imports:

###Part A###
#~~~  implementation of queue class  ~~~
class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue():
	def __init__(self): 
		self.head = None # the first object in the queue
		self.tail = None # the last object in the queue
		self.q_size = 0 # the queue length
        
	def front(self):
		# returns the first object in  the queue
		return self.head
    
	def empty(self):
		# return True if the queue is empty, else False
		return self.head == None

	def enqueue(self, x):
		""" this function is adding an object to the queue"""

		# implements the node class on the new node
		node = Node(x)

		# if the queue is empty the new node will be the head and the tail
		if self.empty() == True:
			self.head = node
			self.tail = node
			self.q_size += 1

		# if the queue is not empty the new node will be the tail
		else:
			self.tail.next = node # the existing tail pointing to the new tail
			self.tail = node # the new node become the tail
			self.q_size += 1

	def dequeue(self):
		""" this function returns the value of the first

		object in the queue and erase it

		"""

		# checks if the queue is empty, if so returns None
		if self.empty():
			return None

		# setting the first node into variable
		X = self.head

		# the next object is stepping into the head
		self.head = self.head.next
		self.q_size -= 1 # the queue is now 1 object shorter

		# checks if the queue have only 1 object
		if self.tail == X:
			self.tail = None
		return X.data


###Part B###
def Was_an_attack(A=list,n=int,t=float):

	""" this function checks if there was an attack according to the data given

	input:
			A: list of lists, each list contains 2 objetcs:
						the name of the request (string)
						the time it was requested (float or int)

			n: number of the same request to define attack

			t: time difference to define attack

	output: list if an attack happened or a 0 else
			the list contains:
				str, attack start time (float), the name of the request (string)
			"""
	if len(A) == 0 or len(A) < n:
		return 0
	if t < 0 or n <= 0:
		raise ValueError("negative parameter")

	# creating a new empty queue
	new_queue = Queue()

	# sort the list given by the time
	A = sorted(A, key= lambda x: x[1]) #O(nlogn)

	# transfer the elements from the list to the queue
	for elem in A: # O(n)
		new_queue.enqueue(elem)

	# while the queue is not empty
	while new_queue.empty() is False: #O(n)
		this_node = new_queue.head

		# potential attack name
		task_lower = this_node.data[0].lower()
		task = this_node.data[0]

		# potential attack start time
		start_time = this_node.data[1]
		counter = 1

		# passes to the next object in the queue
		this_node = this_node.next

		# checks if there was an attack
		if counter == n:
			return ["There was an attack on second " + str(start_time), start_time, task]

		# a loop for every object until the tail
		while this_node is not None:
			if this_node.data[1] - start_time <= t and this_node.data[0].lower() == task_lower:
				counter += 1 # if the conditions are matched, the tasks number rises by 1
				this_node = this_node.next # passing to next object

				# checks if there was an attack
				if counter == n:
					return ["There was an attack on second " + str(start_time), start_time, task]
			else:
				break

		# deletes the first object in the queue
		new_queue.dequeue()
	return 0 # if no attack happened returns 0







