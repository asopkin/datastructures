def HeapSort(A):
	h = []
	for val in A:
		heappush(h, val)
	return [heappop(h) for i in range(len(h))]
