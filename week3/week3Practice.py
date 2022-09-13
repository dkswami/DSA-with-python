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
