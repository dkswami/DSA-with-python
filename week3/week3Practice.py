#unsorted search
def unsortedSearch(seq, v):
	for i in seq:
		if v == i:
			return(True)
	return(False)

def binarySortedSearch(seq,v, l, r):
	if(r-l == 0):
		return(False)
	mid = (l + r)//2
	if(v == seq[mid]):
		return(True)
	if(v < seq[mid]):
		return(binarySortedSearch(seq,v,l,mid))
	else:
		return(binarySortedSearch(seq,v,mid+1,r))

def selectionSort(seq):
	for start in range(len(seq)):
		minipos = start
		for i in range(start, len(seq)):
			if seq[i] < seq[minipos]:
				minipos = i
		(seq[start], seq[minipos]) = (seq[minipos], seq[start])

def insertionSortUsingFor(seq):
	for sliceEnd in range(len(seq)):
		pos = sliceEnd
		for i in range(0, pos):
			if seq[i] > seq[pos]:
				(seq[i], seq[pos]) = (seq[pos], seq[i])

def insertionSortUsingWhile(seq):
	for sliceEnd in range(len(seq)):
		pos = sliceEnd
		while pos >0 and seq[pos] < seq[pos-1]:
			(seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
			pos-1
