import collections
import itertools

#A very basic implementation of a circular buffer queue
#using Python's deque. 

class CircularBufferQueue(object):
	def __init__(self, size=1000):
		self.items = collections.deque(maxlen=size)

	def push(self, item):
		self.items.extend(item)

	def pop(self, size):
		item = []
		for i in range(size):
			item.append(self.items.popleft())
		return item
	def peek(self, size):
		return itertools.islice(self.items, size)
	def len(self):
		return len(self.items)
	def __iter__(self):
		return self
	def get_all(self):
		return(self.items)
	def next(self):
		try:
			size = self.len()
			result = self.peek(size)
		except IndexError:
			raise StopIteration
		return result

test = CircularBufferQueue()
new = [4,3,2]
test.push(new)
print test
size = test.len()
test.pop(size)
print test
test.push(new)
print test.get_all()
test.pop(1)
print test.get_all()
