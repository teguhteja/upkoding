# Python program for implementation of Bubble Sort
  
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
  
# Driver code to test above
arr = [6, 3, 1, 8, 7, 2]
  
bubbleSort(arr)
  
print ("Sorted array is:")
print(arr)