def selectionSort(arr):
  for i in xrange(len(arr)):
    min = i
    for b in xrange(i+1, len(arr)):
      if arr[b] < arr[min]:
        min = b
    arr[i] , arr[min] = arr[min], arr[i] 
  
  print arr
  
arr = [5,3,2,10,45,3,1]
selectionSort(arr)

