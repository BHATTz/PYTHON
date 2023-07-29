'''
def bubbleSort(arr):
	n = len(arr)
	swapped = False
	
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return

arr = [61, 31, 21, 11, 21, 19, 91]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")   '''



def CountFrequency(my_list):

	freq = {}
	for item in my_list:
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1

	for key, value in freq.items():
		print ("% d : % d"%(key, value))

if __name__ == "__main__":
	my_list =[1, 1, 5, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2]

	CountFrequency(my_list)
