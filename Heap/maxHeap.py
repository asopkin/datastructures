# Derived from code on stack overflow.
def maxHeapify(tgt_list, tgt):
	left = (tgt*2)+1
	right = (tgt*2)+2
	biggest = tgt
	if left<len(tgt_list) and tgt_list[left]>tgt_list[biggest]:
		biggest = left
	if right < len(tgt_list) and A[right] > A[biggest]:
		biggest = right
	if biggest != tgt:
		tgt_list[tgt], tgt_list[biggest] = tgt_list[biggest], tgt_list[tgt]
		maxHeapify(tgt_list, biggest)

def build_max_heap(tgt_list):
	for i in range(len(tgt_list)//2, -1, -1):
		maxHeapify(tgt_list, i)
def tree_tester(A, i=0, indent=0):
    if i < len(A):
        print '  ' * indent, A[i]
        tree_tester(A, i * 2 + 1, indent + 1)
        tree_tester(A, i * 2 + 2, indent + 1)

A = range(12)
build_max_heap(A)
print(tree_tester(A))